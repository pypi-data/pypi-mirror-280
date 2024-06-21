from .dev_tool import (
    collect_nodes,
    get_first_node,
    add_indent,
    replace_text,
    insert_text,
)
from typing import Optional, Literal
import ast

# region Manipulate


def get_doc_node(function_node: ast.FunctionDef) -> Optional[ast.Expr]:
    doc_node = None
    if isinstance(function_node.body[0], ast.Expr):
        if type(function_node.body[0].value.value) is str:
            doc_node = function_node.body[0].value

    return doc_node


def insert_before_return_node(function_source: str, text: str) -> str:

    function_node = get_first_node(function_source, ast.FunctionDef)

    return_node: ast.Return = collect_nodes(function_node, ast.Return)[0]
    lineno, col_offset = return_node.lineno - 1, return_node.col_offset

    lines = text.splitlines()
    lines = add_indent(lines, col_offset)

    source_lines = function_source.splitlines()
    source_lines = source_lines[:lineno] + lines + source_lines[lineno:]

    function_source = "\n".join(source_lines)

    return function_source


def insert_after_doc(function_source: str, text: str) -> str:

    function_node = get_first_node(function_source, ast.FunctionDef)
    doc_node = get_doc_node(function_node)

    lineno, col_offset = doc_node.end_lineno, doc_node.col_offset

    lines = text.splitlines()
    lines = add_indent(lines, col_offset)

    source_lines = function_source.splitlines()
    source_lines = source_lines[:lineno] + lines + source_lines[lineno:]

    function_source = "\n".join(source_lines)

    return function_source


def replace_doc(
    function_source: str, text: str, quotations: Literal['"""', "'''"] = '"""'
) -> str:
    if quotations is not None:
        text = quotations + text + quotations

    function_node: ast.FunctionDef = get_first_node(function_source, ast.FunctionDef)

    doc_node = get_doc_node(function_node)
    if doc_node is not None:
        start, end = doc_node.lineno - 1, doc_node.end_lineno
        indent = doc_node.col_offset
        function_source = replace_text(start, end, indent, function_source, text)
    else:
        first_node = function_node.body[0]
        index = first_node.lineno - 1
        indent = first_node.col_offset
        function_source = insert_text(index, indent, function_source, text)
    return function_source
