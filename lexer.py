import re
from dataclasses import dataclass


# Represents one token
@dataclass
class Token:
    type: str
    value: str
    position: int


# Token patterns
TOKEN_SPEC = [
    ("NUMBER", r"(?:\d+\.\d+|\d+)"),
    ("ID", r"[A-Za-z_][A-Za-z0-9_]*"),
    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("MULT", r"\*"),
    ("DIV", r"/"),
    ("POW", r"\^"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("COMMA", r","),
    ("SKIP", r"[ \t]+"),
    ("MISMATCH", r"."),
]


# Combine all patterns into one regular expression
TOKEN_REGEX = "|".join(
    f"(?P<{name}>{pattern})"
    for name, pattern in TOKEN_SPEC
)


# Built-in functions
KEYWORDS = {
    "sqrt": "SQRT",
    "pow": "POW_FUNC",
}


def tokenize(text):
    tokens = []

    for match in re.finditer(TOKEN_REGEX, text):

        token_type = match.lastgroup
        value = match.group()
        position = match.start()

        # Ignore spaces and tabs
        if token_type == "SKIP":
            continue

        # Check whether an identifier is a built-in function
        if token_type == "ID":
            token_type = KEYWORDS.get(value, "ID")

        # Invalid character
        if token_type == "MISMATCH":
            raise SyntaxError(
                f"Invalid character '{value}' "
                f"at position {position}"
            )

        tokens.append(
            Token(token_type, value, position)
        )

    # End of input
    tokens.append(
        Token("EOF", "", len(text))
    )

    return tokens


# Test the lexical analyzer
if __name__ == "__main__":

    formula = "sqrt(x^2 + 25)"

    print("Input:")
    print(formula)

    print("\nTokens:")

    tokens = tokenize(formula)

    for token in tokens:
        print(token)