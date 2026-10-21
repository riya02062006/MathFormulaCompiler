
from ast_nodes import (
    NumberNode,
    VariableNode,
    BinaryOp,
    UnaryOp,
    FunctionNode
)


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    # Return the current token
    def current(self):
        return self.tokens[self.position]

    # Check the expected token and move forward
    def consume(self, token_type):
        token = self.current()

        if token.type != token_type:
            raise SyntaxError(
                f"Expected {token_type}, "
                f"found {token.type} "
                f"at position {token.position}"
            )

        self.position += 1
        return token

    # Start parsing the formula
    def parse(self):
        node = self.expression()

        if self.current().type != "EOF":
            token = self.current()

            raise SyntaxError(
                f"Unexpected token '{token.value}' "
                f"at position {token.position}"
            )

        return node

    # Handle addition and subtraction
    def expression(self):
        node = self.term()

        while self.current().type in ("PLUS", "MINUS"):
            operator = self.consume(self.current().type)
            right = self.term()

            node = BinaryOp(
                operator.value,
                node,
                right
            )

        return node

    # Handle multiplication and division
    def term(self):
        node = self.unary()

        while self.current().type in ("MULT", "DIV"):
            operator = self.consume(self.current().type)
            right = self.unary()

            node = BinaryOp(
                operator.value,
                node,
                right
            )

        return node

    # Handle unary plus and minus
    def unary(self):
        if self.current().type == "PLUS":
            self.consume("PLUS")
            return UnaryOp("+", self.unary())

        if self.current().type == "MINUS":
            self.consume("MINUS")
            return UnaryOp("-", self.unary())

        return self.power()

    # Handle exponentiation
    # Exponentiation binds more tightly than a leading unary sign
    def power(self):
        node = self.atom()

        if self.current().type == "POW":
            self.consume("POW")
            right = self.unary()

            node = BinaryOp(
                "^",
                node,
                right
            )

        return node

    # Handle numbers, variables, parentheses and functions
    def atom(self):
        token = self.current()

        # Number
        if token.type == "NUMBER":
            self.consume("NUMBER")
            return NumberNode(token.value)

        # Variable
        if token.type == "ID":
            self.consume("ID")
            return VariableNode(token.value)

        # Parenthesized expression
        if token.type == "LPAREN":
            self.consume("LPAREN")
            node = self.expression()
            self.consume("RPAREN")
            return node

        # sqrt(expression)
        if token.type == "SQRT":
            self.consume("SQRT")
            self.consume("LPAREN")

            argument = self.expression()

            self.consume("RPAREN")

            return FunctionNode("sqrt", [argument])

        # pow(expression, expression)
        if token.type == "POW_FUNC":
            self.consume("POW_FUNC")
            self.consume("LPAREN")

            first = self.expression()
            self.consume("COMMA")
            second = self.expression()

            self.consume("RPAREN")

            return FunctionNode("pow", [first, second])

        # Incomplete expression
        if token.type == "EOF":
            raise SyntaxError(
                f"Incomplete expression at position "
                f"{token.position}: expected a number, "
                f"variable, function, or parenthesized expression."
            )

        # Unexpected token
        raise SyntaxError(
            f"Unexpected token '{token.value}' "
            f"at position {token.position}"
        )
