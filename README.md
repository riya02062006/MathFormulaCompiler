# MathFormulaCompiler

A Python-based mini compiler that validates mathematical formulas using lexical analysis, syntax analysis, Abstract Syntax Tree (AST) generation, and semantic analysis.

## 1. Project Overview

The Mathematical Formula Compiler is designed to validate mathematical expressions involving variables, constants, arithmetic operators, exponentiation, parentheses, and built-in functions such as `sqrt()` and `pow()`.

The project demonstrates the fundamental phases of compiler design through a simple Python implementation.

## 2. Features

- Lexical analysis and token generation
- Syntax analysis using recursive-descent parsing
- Support for arithmetic operators and exponentiation
- Support for unary operators and parentheses
- Support for `sqrt()` and `pow()` functions
- Abstract Syntax Tree generation and printing
- Selected semantic error detection
- Error reporting for invalid formulas

## 3. Requirements

- Python 3
- Git
- GitHub account
- Visual Studio Code or another Python editor

No external Python packages are required for the current implementation.

## 4. How to Run

Clone the repository:

```bash
git clone https://github.com/riya02062006/MathFormulaCompiler.git
```

Navigate to the project directory:

```bash
cd MathFormulaCompiler
```

Run the compiler:

```bash
py main.py
```

Alternatively, use `python main.py` if that is the Python command configured on your computer.

## 5. Compiler Phases

### Lexical Analysis

The lexical analyzer identifies tokens such as variables, numbers, arithmetic operators, parentheses, and mathematical functions. It reports invalid characters.

### Syntax Analysis

The parser checks whether the input formula follows the defined grammar and handles operator precedence and associativity.

### Abstract Syntax Tree

The AST represents the structure of a parsed mathematical formula using different node types. The AST printer displays the tree in a readable format.

### Semantic Analysis

The semantic analyzer checks selected conditions, including division by a numeric constant equal to zero, directly represented negative constants passed to `sqrt()`, and the expected number of function arguments.

## 6. Grammar and Transformations

The file `grammar.txt` contains the context-free grammar for mathematical formulas and the grammar after eliminating immediate left recursion from the expression and term productions.

It describes the grammar rules for arithmetic expressions, variables, numeric constants, exponentiation, parentheses, and built-in functions.

## 7. Testing

The `tests/` directory contains sample valid and invalid formulas.

Examples of valid formulas:

- `x + 5`
- `sqrt(x^2 + 25)`
- `pow(x, 2)`
- `3 * (x + 4)^2`
- `sqrt(pow(x, 2) + pow(y, 2))`

Examples of invalid formulas:

- `sqrt(-9)` — selected semantic error
- `x + @` — lexical error
- `x +` — syntax error

The actual test results depend on the implemented lexer, parser, and semantic checks.

## 8. Project Structure
## Project Structure

```text
MathFormulaCompiler/
├── main.py
├── gui.py
├── lexer.py
├── parser.py
├── ast_nodes.py
├── ast_printer.py
├── semantic.py
├── grammar.txt
├── README.md
├── tests/
│   ├── valid_tests.txt
│   └── invalid_tests.txt
└── screenshots/
    ├── output_1.png
    ├── output_2.png
    ├── output_3.png
    └── output_4.png
```

### File Descriptions



 1.`main.py` :  Main program for running and testing the compiler |
 2.`gui.py` : Graphical user interface for entering and validating mathematical formulas |
 3.`lexer.py` : Performs lexical analysis and generates tokens |
 4.`parser.py` : Performs syntax analysis and constructs the Abstract Syntax Tree |
 5.`ast_nodes.py` : Defines the different AST node classes |
 6.`ast_printer.py` : Displays the Abstract Syntax Tree in a readable format |
 7.`semantic.py` : Performs semantic validation and detects selected mathematical errors |
 8.`grammar.txt` : Contains the context-free grammar and grammar transformations |
 9.`tests/` : Contains valid and invalid mathematical formula test cases |
 10.`screenshots/` : Contains screenshots of compiler and GUI execution |
 11.`README.md` : Contains project information, instructions, documentation, and contribution details |




## 10. Documentation and Project Resources

The repository includes the following project resources:

- **README.md:** Project overview, features, requirements, execution instructions, architecture, file descriptions, and contributor responsibilities.
- **grammar.txt:** Context-free grammar and grammar transformation details.
- **tests/valid_tests.txt:** Valid formula test cases.
- **tests/invalid_tests.txt:** Invalid formula test cases.
- **compiler_output.png:** Screenshot showing compiler execution and output.
- **Source files:** Implementation of the lexer, parser, AST, AST printer, semantic analyzer, and main program.

Additional documents, reports, presentation slides, and screenshots can be maintained in dedicated folders as they are created.

## 11. Team Contributions

The project is divided among six members. The following table describes the planned responsibilities and the files or resources associated with each contribution.


1. Member 1 : `README.md`, project report. 
2. Member 2 : `parser.py`, `semantic.py` .
3. Member 3 : `lexer.py`, token documentation.
4. Member 4 : `tests/valid_tests.txt`, `tests/invalid_tests.txt`, `compiler_output.png` , Testing and output screenshots.
5. Member 5 : `ast_nodes.py`, `ast_printer.py`, AST documentation.
6. Member 6 :  Presentation slides and supporting documentation.

*The table describes the planned division of work. Update it to reflect the actual contributions and files created or modified by each member.*

## 12. GitHub Collaboration

Each member should contribute to the shared repository through their own GitHub account.

The contribution workflow includes:

1. Working on the assigned source file or documentation.
2. Testing the changes where applicable.
3. Committing the changes with a meaningful commit message.
4. Pushing the contribution to GitHub.
5. Reviewing the final changes before merging.

Contributions should represent actual work performed by each member.

## 13. Limitations

- The compiler does not evaluate every expression to a numerical result.
- Variables are not resolved using a symbol table.
- Semantic checks cover only selected mathematical conditions.
- Error recovery is limited.
- The project is intended for educational purposes.

## 14. Future Enhancements

- Mathematical expression evaluation
- Symbol-table implementation
- Expanded semantic analysis
- Improved error messages
- Automated testing
- Graphical user interface
- Enhanced AST visualization

## 15. Conclusion

The Mathematical Formula Compiler demonstrates important compiler-design concepts, including lexical analysis, syntax analysis, grammar transformations, AST generation, and semantic validation. The modular implementation provides a foundation for further development and improvement.


