import streamlit as st
from lexer import tokenize
from parser import Parser
from ast_printer import print_ast
from semantic import SemanticAnalyzer

st.set_page_config(page_title="Mathematical Formula Compiler")

st.title("Mathematical Formula Compiler")
st.write("Enter a mathematical formula to validate it.")

formula = st.text_input(
    "Enter formula",
    placeholder="Example: sqrt(x^2 + 25)"
)

if st.button("Validate Formula"):
    if formula.strip():
        try:
            tokens = tokenize(formula)
            ast = Parser(tokens).parse()

            analyzer = SemanticAnalyzer()
            analyzer.analyze(ast)

            st.success("Formula is valid!")

            st.subheader("Tokens")
            st.write(tokens)

            st.subheader("Abstract Syntax Tree (AST)")
            st.code(str(print_ast(ast)))

        except Exception as error:
            st.error(f"Formula validation failed: {error}")
    else:
        st.warning("Please enter a formula.")
