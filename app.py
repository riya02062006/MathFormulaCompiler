
import streamlit as st
from contextlib import redirect_stdout
from io import StringIO

from lexer import tokenize
from parser import Parser
from ast_printer import print_ast
from semantic import SemanticAnalyzer, SemanticError

st.set_page_config(
    page_title="Mathematical Formula Compiler",
    page_icon="🧮",
    layout="centered"
)

st.title("Mathematical Formula Compiler")
st.write(
    "Validate mathematical formulas using lexical, "
    "syntactic, and semantic analysis."
)

st.info(
    "Examples: x + 5, sqrt(x^2 + 25), "
    "pow(x, 2), 3 * (x + 4)^2"
)

formula = st.text_input(
    "Enter a mathematical formula",
    placeholder="sqrt(x^2 + 25)"
)

if st.button("Validate Formula", type="primary"):
    if not formula.strip():
        st.warning("Please enter a formula.")
    else:
        try:
            # Stage 1: Lexical analysis
            tokens = tokenize(formula)

            # Stage 2: Syntax analysis and AST creation
            ast = Parser(tokens).parse()

            # Stage 3: Semantic analysis
            SemanticAnalyzer().analyze(ast)

            st.success("Formula is valid!")

            with st.expander("View Tokens"):
                for token in tokens:
                    st.write(
                        f"Type: {token.type} | "
                        f"Value: {token.value} | "
                        f"Position: {token.position}"
                    )

            with st.expander("View Abstract Syntax Tree"):
                output = StringIO()
                with redirect_stdout(output):
                    print_ast(ast)

                st.code(output.getvalue(), language="text")

        except SemanticError as error:
            st.error(f"Semantic Error: {error}")

        except SyntaxError as error:
            st.error(f"Syntax Error: {error}")

        except Exception as error:
            st.error(f"Error: {error}")
