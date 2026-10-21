
from ast_nodes import (
    NumberNode,
    VariableNode,
    BinaryOp,
    UnaryOp,
    FunctionNode
)


def print_ast(node, indent=0):
    prefix = " " * indent

    if isinstance(node, NumberNode):
        print(prefix + f"Number: {node.value}")

    elif isinstance(node, VariableNode):
        print(prefix + f"Variable: {node.name}")

    elif isinstance(node, BinaryOp):
        print(prefix + f"Operator: {node.operator}")
        print_ast(node.left, indent + 4)
        print_ast(node.right, indent + 4)

    elif isinstance(node, UnaryOp):
        print(prefix + f"Unary Operator: {node.operator}")
        print_ast(node.operand, indent + 4)

    elif isinstance(node, FunctionNode):
        print(prefix + f"Function: {node.name}")

        for argument in node.arguments:
            print_ast(argument, indent + 4)
