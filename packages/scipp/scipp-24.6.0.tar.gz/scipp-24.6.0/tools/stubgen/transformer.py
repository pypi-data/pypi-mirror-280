"""Transform an AST to fix type annotations."""

import ast
import inspect

from .config import CPP_CORE_MODULE_NAME


def unqualified_cpp_class(node: ast.Attribute | ast.Name) -> str | None:
    """Return the unqualified name of a C++ class in _scipp.core.
    Returns None if the class is not in _scipp.core.
    ``node`` should be a type annotation.
    """
    pieces = []
    while isinstance(node, ast.Attribute):
        pieces.append(node.attr)
        node = node.value
    pieces.append(node.id)
    if pieces[1:] != CPP_CORE_MODULE_NAME.split('.')[::-1]:
        return None
    return pieces[0]


def replace_function(base: ast.FunctionDef, **kwargs) -> ast.FunctionDef:
    args = {
        'name': base.name,
        'args': base.args,
        'body': base.body,
        'decorator_list': base.decorator_list,
        'returns': base.returns,
        'type_comment': base.type_comment,
    }
    return ast.FunctionDef(**{**args, **kwargs})


def add_decorator(
    base: ast.FunctionDef, decorator: ast.Name | ast.Attribute
) -> ast.FunctionDef:
    return replace_function(base, decorator_list=[decorator, *base.decorator_list])


def get_first_argument(node: ast.arguments) -> ast.arg:
    if node.posonlyargs:
        return node.posonlyargs[0]
    return node.args[0]


class AddOverloadedDecorator(ast.NodeTransformer):
    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        self.generic_visit(node)
        return add_decorator(node, decorator=ast.Name(id='overload', ctx=ast.Load()))


class RemoveDecorators(ast.NodeTransformer):
    """Remove n innermost decorators from a function."""

    def __init__(self, n: int) -> None:
        self.n = n

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        self.generic_visit(node)
        decorators = node.decorator_list
        return replace_function(
            node, decorator_list=decorators[: len(decorators) - self.n]
        )


class FixSelfArgName(ast.NodeTransformer):
    """Ensure that the first argument is called self."""

    def visit_arguments(self, node: ast.arguments) -> ast.arguments:
        self.generic_visit(node)
        keep = {
            'kwonlyargs': node.kwonlyargs,
            'vararg': node.vararg,
            'kwarg': node.kwarg,
            'kw_defaults': node.kw_defaults,
            'defaults': node.defaults,
        }
        if node.posonlyargs and node.posonlyargs[0].arg != 'self':
            return ast.arguments(
                posonlyargs=[
                    ast.arg('self', annotation=None, type_comment=None),
                    *node.posonlyargs[1:],
                ],
                args=node.args,
                **keep,
            )
        if not node.posonlyargs and node.args and node.args[0].arg != 'self':
            return ast.arguments(
                args=[
                    ast.arg('self', annotation=None, type_comment=None),
                    *node.args[1:],
                ],
                posonlyargs=node.posonlyargs,
                **keep,
            )
        return node


class DropSelfAnnotation(ast.NodeTransformer):
    """Remove type annotations from 'self' argument."""

    def visit_arg(self, node: ast.arg) -> ast.arg:
        if node.arg != 'self':
            self.generic_visit(node)
            return node
        return ast.arg(node.arg, None, None)


class ReplaceTypeVarInReturn(ast.NodeTransformer):
    """Replace TypeVars in return annotations with concrete types.

    Some functions are defined as generic functions in Python, e.g.,

    .. code-block:: python

        def sum(x: VariableLikeType, dim: Dims = None) -> VariableLikeType:

    When those functions are bound as methods, the return type is constrained by
    the class that the method is bound to.
    So this transformer replaces the annotation by the class name.
    """

    TYPE_VARS = ('VariableLikeType', '_VarDaDg')

    def __init__(self, cls_name: str) -> None:
        self.cls_name = cls_name

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        self.generic_visit(node)
        for type_var in self.TYPE_VARS:
            if isinstance(node.returns, ast.Name) and node.returns.id == type_var:
                first_arg = get_first_argument(node.args)
                try:
                    self_annotation = first_arg.annotation.id
                except AttributeError:
                    continue
                if self_annotation == type_var:
                    return replace_function(
                        node, returns=ast.Name(id=self.cls_name, ctx=ast.Load())
                    )
        return node


class ShortenCppClassAnnotation(ast.NodeTransformer):
    """Remove module qualification from scipp classes."""

    def visit_Attribute(self, node: ast.Attribute) -> ast.Attribute | ast.Name:
        self.generic_visit(node)
        if (cls := unqualified_cpp_class(node)) is not None:
            return ast.Name(cls)
        if isinstance(node.value, ast.Name) and node.value.id == '_cpp':
            return ast.Name(id=node.attr, ctx=ast.Load())
        return node


class DropTypingModule(ast.NodeTransformer):
    def visit_Attribute(self, node: ast.Attribute) -> ast.Attribute | ast.Name:
        self.generic_visit(node)
        if isinstance(node.value, ast.Name) and node.value.id == 'typing':
            return ast.Name(id=node.attr, ctx=ast.Load())
        return node


class DropFunctionBody(ast.NodeTransformer):
    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        self.generic_visit(node)
        if (
            node.body
            and isinstance(node.body[0], ast.Expr)
            and isinstance(node.body[0].value, ast.Constant)
        ):
            new_body = [ast.Expr(value=ast.Constant(value=node.body[0].value.value))]
        else:
            new_body = [ast.Expr(value=ast.Constant(value=Ellipsis))]
        return replace_function(node, body=new_body)


class SetFunctionName(ast.NodeTransformer):
    def __init__(self, name: str) -> None:
        self.target_name = name

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        self.generic_visit(node)
        return replace_function(node, name=self.target_name)


class OverwriteSignature(ast.NodeTransformer):
    """Replaces a function signature by the given signature."""

    def __init__(self, sig: inspect.Signature) -> None:
        self.sig = sig

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        self.generic_visit(node)
        code = f'def f{self.sig}: ...'
        # A hack to work around _NoDefault.__repr__
        # I can't think of a better way to do this :(
        code = code.replace('NotSpecified', '_NoDefault')
        target = ast.parse(code).body[0]
        r = replace_function(
            node,
            args=target.args,
            returns=target.returns,
        )
        return r


class FixArgumentFromSupertypes(ast.NodeTransformer):
    def __init__(self) -> None:
        self._do_replacement = False

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        if node.name in ('__eq__', '__ne__'):
            self._do_replacement = True
        self.generic_visit(node)
        self._do_replacement = False
        return node

    def visit_arg(self, node: ast.arg) -> ast.arg:
        if self._do_replacement and node.arg != 'self':
            return ast.arg(
                arg=node.arg, annotation=ast.Name('object'), type_comment=None
            )
        return node


class FixObjectReturnType(ast.NodeTransformer):
    METHODS = (
        '__iadd__',
        '__iand__',
        '__iconcat__',
        '__ifloordiv__',
        '__ilshift__',
        '__imatmul__',
        '__imod__',
        '__imul__',
        '__ior__',
        '__ipow__',
        '__irshift__' '__isub__',
        '__itruediv__',
        '__ixor__',
    )

    def __init__(self, cls: str | None) -> None:
        self.cls = cls

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        self.generic_visit(node)
        if (
            node.name in self.METHODS
            and isinstance(node.returns, ast.Name)
            and node.returns.id in ('Any', 'object')
        ):
            return replace_function(node, returns=ast.Name(self.cls))
        return node


class ObjectToAny(ast.NodeTransformer):
    def visit_Name(self, node: ast.Name) -> ast.Name:
        if node.id == 'object':
            return ast.Name(id='Any', ctx=ast.Load())
        return node


class ReplaceNoneType(ast.NodeTransformer):
    def visit_Name(self, node: ast) -> ast.Name:
        if node.id == 'NoneType':
            return ast.Name(id='None', ctx=ast.Load())
        return node


class RemoveDocstring(ast.NodeTransformer):
    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        self.generic_visit(node)
        return replace_function(
            node, body=[ast.Expr(value=ast.Constant(value=Ellipsis))]
        )


def _fix_common(node: ast.AST) -> ast.AST:
    node = FixSelfArgName().visit(node)
    node = DropSelfAnnotation().visit(node)
    node = ShortenCppClassAnnotation().visit(node)
    node = ObjectToAny().visit(node)
    node = ReplaceNoneType().visit(node)
    node = DropTypingModule().visit(node)
    return node


def fix_method(node: ast.AST, cls_name: str) -> ast.AST:
    node = ReplaceTypeVarInReturn(cls_name).visit(node)  # Must be before FixSelfArgName
    node = _fix_common(node)
    node = FixObjectReturnType(cls_name).visit(node)
    node = FixArgumentFromSupertypes().visit(node)
    node = ast.fix_missing_locations(node)
    return node


def fix_property(node: ast.AST) -> ast.AST:
    node = _fix_common(node)
    node = ast.fix_missing_locations(node)
    return node
