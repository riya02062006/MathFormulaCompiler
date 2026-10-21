class NumberNode:
    def __init__(self, value):
        self.value = value


class VariableNode:
    def __init__(self, name):
        self.name = name


class BinaryOp:
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right


class UnaryOp:
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand


class FunctionNode:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments


if __name__ == "__main__":
    number = NumberNode("25")
    variable = VariableNode("x")

    addition = BinaryOp("+", variable, number)

    print("AST created successfully!")
    print(addition.operator)
    print(addition.left.name)
    print(addition.right.value)