from .dev_tool import (
    safe_unparse,
    collect_nodes,
)
from .specs import ArgSpec, ReturnSpec, FuncSpec
from typing import List, Optional
import ast
from ast import unparse

# region Extract Args


def extract_positional_arg_specs(function_node: ast.FunctionDef) -> List[ArgSpec]:
    arg_specs = []
    arguments_node: ast.arguments = collect_nodes(function_node, ast.arguments)[0]
    arg_nodes: List[ast.arg] = arguments_node.args
    defaults: List[str] = [unparse(default) for default in arguments_node.defaults]

    defaults_start = len(arg_nodes) - len(defaults)
    defaults = [None] * defaults_start + defaults

    for i, arg_node in enumerate(arg_nodes):
        if arg_node.annotation is not None:
            annotation = unparse(arg_node.annotation)
        else:
            annotation = None
        arg_specs.append(
            ArgSpec(
                name=arg_node.arg,
                type="positional",
                annotation=annotation,
                default=defaults[i],
            )
        )

    return arg_specs


def extract_special_arg_specs(function_node: ast.FunctionDef) -> List[ArgSpec]:
    arg_specs = []
    arguments_node: ast.arguments = collect_nodes(function_node, ast.arguments)[0]

    if arguments_node.vararg is not None:
        vararg = arguments_node.vararg
        arg_specs.append(
            ArgSpec(
                name=vararg.arg,
                type="vararg",
                annotation=safe_unparse(vararg.annotation),
            )
        )

    if len(arguments_node.kwonlyargs) != 0:
        for i, kwonlyarg in enumerate(arguments_node.kwonlyargs):
            arg_specs.append(
                ArgSpec(
                    name=kwonlyarg.arg,
                    type="kwonlyarg",
                    annotation=safe_unparse(kwonlyarg.annotation),
                    default=safe_unparse(arguments_node.kw_defaults[i]),
                )
            )

    if arguments_node.kwarg is not None:
        kwarg = arguments_node.kwarg
        arg_specs.append(
            ArgSpec(
                name=kwarg.arg,
                type="kwarg",
                annotation=safe_unparse(kwarg.annotation),
            )
        )

    return arg_specs


# endregion

# region Extract Returns


def extract_return_specs(function_node: ast.FunctionDef) -> List[ReturnSpec]:
    return_specs = []
    return_node: ast.Return = collect_nodes(function_node, ast.Return)[0]
    if all(
        [
            isinstance(return_node.value, ast.Tuple),
            function_node.returns.value.id == "Tuple",
        ]
    ):
        return_names = [unparse(elt) for elt in return_node.value.elts]
        return_typehints = [unparse(elt) for elt in function_node.returns.slice.elts]
        if len(return_names) != len(return_typehints):
            raise "Type Hints have some problem. The number of annotation in Tuple type hints should be the same as the number of returns."

        for return_name, return_typehint in zip(return_names, return_typehints):
            return_specs.append(
                ReturnSpec(name=return_name, annotation=return_typehint)
            )
    else:
        return_specs.append(
            ReturnSpec(
                name=unparse(return_node.value),
                annotation=safe_unparse(function_node.returns),
            )
        )

    return return_specs


# endregion


# region Extract FuncSpec


def extract_doc(function_node: ast.FunctionDef) -> Optional[str]:
    if isinstance(function_node.body[0], ast.Expr):
        if type(function_node.body[0].value.value) is str:
            return function_node.body[0].value.value

    return None


def extract_func_spec(function_node: ast.FunctionDef) -> FuncSpec:
    name = function_node.name
    doc = extract_doc(function_node)
    arg_specs = []
    arg_specs += extract_positional_arg_specs(function_node)
    arg_specs += extract_special_arg_specs(function_node)
    return_specs = extract_return_specs(function_node)

    func_spec = FuncSpec(
        name=name, doc=doc, arg_specs=arg_specs, return_specs=return_specs
    )

    return func_spec


# endregion
