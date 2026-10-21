
from lexer import tokenize
from parser import Parser
from semantic import SemanticAnalyzer, SemanticError
from ast_printer import print_ast


test_formulas = [
    "x + 5",
    "sqrt(x^2 + 25)",
    "pow(x, 2)",
    "3 * (x + 4)^2",
    "sqrt(pow(x, 2) + pow(y, 2))",
    "-x^2",
    "sqrt(-9)",
    "x + @"
]
analyzer = SemanticAnalyzer()

for formula in test_formulas:
    print("\nFormula:", formula)

    try:
        tokens = tokenize(formula)
        parser = Parser(tokens)
        ast = parser.parse()

        
        print("Syntax check: Passed")

        analyzer.analyze(ast)

        print("Semantic check: Passed")
        print("\nAbstract Syntax Tree:")
        print_ast(ast)

        print("Result: Valid formula")

    except (SyntaxError, SemanticError) as error:
        print("Result: Invalid formula")
        print("Reason:", error)
