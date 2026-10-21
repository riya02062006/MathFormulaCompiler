
# Mathematical Formula Compiler Front End

## 1. Project Overview

This project implements a compiler front end that validates mathematical formulas containing variables, numeric constants, arithmetic operators, exponentiation, parentheses, and built-in functions such as `sqrt()` and `pow()`.

The compiler checks the lexical structure and syntax of formulas, constructs an Abstract Syntax Tree (AST), and performs basic semantic validation.

## 2. Objectives

- Recognize tokens in mathematical formulas.
- Validate formulas using a parser.
- Construct and display an Abstract Syntax Tree.
- Check semantic errors such as division by zero.
- Validate supported built-in functions.
- Display meaningful error messages for invalid formulas.

## 3. Features

- Variables and numeric constants
- Addition, subtraction, multiplication, and division
- Exponentiation using `^`
- Unary plus and minus
- Parentheses
- Built-in functions: `sqrt()` and `pow()`
- Syntax error detection
- Semantic error detection
- AST generation and display

## 4. Technologies Used

- Python 3
- Visual Studio Code
- Git and GitHub

## 5. Project Structure

```text
MathFormulaCompiler/
├── main.py
├── lexer.py
├── parser.py
├── ast_nodes.py
├── ast_printer.py
├── semantic.py
├── tests/
│   ├── valid_tests.txt
│   └── invalid_tests.txt
└── README.md
```

## 6. Compiler Architecture

The project follows these stages:

1. **Lexical Analysis:** Converts the input formula into tokens.
2. **Syntax Analysis:** Checks the grammatical structure and builds an AST.
3. **Semantic Analysis:** Checks selected semantic errors, including division by zero and square roots of negative numeric constants.
4. **AST Display:** Displays the tree structure of formulas that pass all checks.

## 7. How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in a terminal.
4. Run:

```bash
py main.py
```

The program tests the formulas listed in `main.py` and displays validation results.

## 8. Sample Test Cases

| Formula | Expected outcome |
|---|---|
| `x + 5` | Valid |
| `sqrt(x^2 + 25)` | Valid |
| `pow(x, 2)` | Valid |
| `pow(x)` | Invalid syntax |
| `10 / 0` | Semantic error |
| `sqrt(-9)` | Semantic error |
| `x + @` | Lexical error |
| `x +` | Syntax error |

## 9. Limitations

- The program validates formulas; it does not evaluate their numerical results.
- Variables are not assigned values or checked against a symbol table.
- Semantic analysis covers selected errors rather than every possible mathematical domain error.
- Function argument counts are enforced by the parser.

## 10. Future Enhancements

- Add variable declarations and symbol-table support.
- Expand semantic validation.
- Add a graphical user interface.
- Generate more detailed parse-tree visualizations.
- Add automated tests.

## 11. Contributors

Add the names of all project team members and describe each person's contribution here.
