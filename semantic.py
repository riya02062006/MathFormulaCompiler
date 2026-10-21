
from ast_nodes import (
    NumberNode,
    VariableNode,
    BinaryOp,
    UnaryOp,
    FunctionNode
)


class SemanticError(Exception):
    pass


class SemanticAnalyzer:

    def analyze(self, node):

        # Check binary operations such as +, -, *, /, ^
        if isinstance(node, BinaryOp):

            self.analyze(node.left)
            self.analyze(node.right)

            # Detect division by zero
            if node.operator == "/":
                if (
                    isinstance(node.right, NumberNode)
                    and float(node.right.value) == 0
                ):
                    raise SemanticError(
                        "Division by zero is not allowed."
                    )

        # Check unary plus and minus
        elif isinstance(node, UnaryOp):

            self.analyze(node.operand)

        # Check built-in functions
        elif isinstance(node, FunctionNode):

            expected_arguments = {
                "sqrt": 1,
                "pow": 2
            }

            expected = expected_arguments.get(node.name)

            if expected is None:
                raise SemanticError(
                    f"Unknown function '{node.name}'."
                )

            actual = len(node.arguments)

            if actual != expected:
                raise SemanticError(
                    f"Function '{node.name}' expects "
                    f"{expected} argument(s), "
                    f"but received {actual}."
                )

            # Analyze each argument
            for argument in node.arguments:
                self.analyze(argument)

            # Check sqrt of a negative numeric constant
            if node.name == "sqrt":
                argument = node.arguments[0]

                if isinstance(argument, NumberNode):
                    value = float(argument.value)

                elif (
                    isinstance(argument, UnaryOp)
                    and argument.operator == "-"
                    and isinstance(
                        argument.operand, NumberNode
                    )
                ):
                    value = -float(
                        argument.operand.value
                    )

                else:
                    value = None

                if value is not None and value < 0:
                    raise SemanticError(
                        "Square root of a negative number "
                        "is not allowed in real arithmetic."
                    )

        # Numbers and variables need no additional checks
        elif isinstance(node, (NumberNode, VariableNode)):
            pass

        else:
            raise SemanticError("Unknown AST node.")
