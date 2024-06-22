from typing import Optional, List, Type
import ast
from ast import unparse, parse


class NodeCollector(ast.NodeVisitor):
    def __init__(self, node_type: Type[ast.AST]):
        self.node_type = node_type
        self.nodes = []

    def visit(self, node: ast.AST):
        if isinstance(node, self.node_type):
            self.nodes.append(node)
        self.generic_visit(node)


def collect_nodes(tree: ast.AST, node_type: Type[ast.AST]) -> List[ast.AST]:
    collector = NodeCollector(node_type)
    collector.visit(tree)
    return collector.nodes


def print_node(node: ast.AST, indent=2) -> None:
    print(ast.dump(node, indent=indent))


def print_sources(sources: List[str], divider: str = "\n####################") -> None:
    for source in sources:
        print(divider)
        print(source)


def get_node(source: str) -> ast.AST:
    return ast.parse(source)


def get_sources(source: str, node_type: Type[ast.AST]) -> List[str]:
    tree = parse(source)
    nodes = collect_nodes(tree, node_type)
    sources = [unparse(node) for node in nodes]
    return sources


def print_source_as_node(source: str):
    node = get_node(source)
    print_node(node)


def safe_unparse(node: Optional[ast.AST]) -> Optional[str]:
    if node is not None:
        output = unparse(node)
    else:
        output = None
    return output


def get_first_node(source: str, node_type: Type[ast.AST]) -> Optional[ast.AST]:
    tree = get_node(source)
    nodes = collect_nodes(tree, node_type)
    if len(nodes) == 0:
        node = None
    else:
        node = nodes[0]
    return node


def add_indent(lines: List[str], indent: int = 4) -> List[str]:
    new_lines = []
    for line in lines:
        new_lines.append(" " * indent + line)

    return new_lines


def insert_text(index: int, indent: int, text: str, new_text: str):
    lines = text.splitlines()
    new_lines = new_text.splitlines()

    new_lines = add_indent(new_lines, indent=indent)

    lines = lines[:index] + new_lines + lines[index:]
    text = "\n".join(lines)
    return text


def replace_text(start: int, end: int, indent: int, text: str, new_text: str):
    lines = text.splitlines()
    new_lines = new_text.splitlines()

    new_lines = add_indent(new_lines, indent=indent)

    lines = lines[:start] + new_lines + lines[end:]
    text = "\n".join(lines)
    return text
