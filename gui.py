
import tkinter as tk
from tkinter import ttk
from contextlib import redirect_stdout
from io import StringIO

from lexer import tokenize
from parser import Parser
from semantic import SemanticAnalyzer, SemanticError
from ast_printer import print_ast


class MathFormulaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Formula Compiler")
        self.root.geometry("850x680")
        self.root.minsize(700, 580)
        self.root.configure(bg="#f1f5f9")

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "TButton",
            font=("Segoe UI", 10),
            padding=8
        )

        header = tk.Frame(self.root, bg="#172554", pady=18)
        header.pack(fill="x")

        tk.Label(
            header,
            text="MATH FORMULA COMPILER",
            font=("Segoe UI", 21, "bold"),
            fg="white",
            bg="#172554"
        ).pack()

        tk.Label(
            header,
            text="Lexical Analysis  |  Syntax Analysis  |  Semantic Analysis",
            font=("Segoe UI", 10),
            fg="#bfdbfe",
            bg="#172554"
        ).pack(pady=(5, 0))

        main = tk.Frame(self.root, bg="#f1f5f9", padx=22, pady=18)
        main.pack(fill="both", expand=True)

        tk.Label(
            main,
            text="Enter a mathematical formula",
            font=("Segoe UI", 12, "bold"),
            bg="#f1f5f9",
            fg="#172554"
        ).pack(anchor="w")

        self.formula = tk.Entry(
            main,
            font=("Consolas", 14),
            relief="solid",
            bd=1
        )
        self.formula.pack(fill="x", pady=(8, 10), ipady=9)
        self.formula.insert(0, "sqrt(x^2 + 25)")
        self.formula.bind("<Return>", lambda event: self.validate())

        examples = tk.Frame(main, bg="#f1f5f9")
        examples.pack(fill="x", pady=(0, 12))

        tk.Label(
            examples,
            text="Try an example:",
            bg="#f1f5f9",
            fg="#475569"
        ).pack(side="left", padx=(0, 8))

        for example in ["x + 5", "pow(x, 2)", "sqrt(-9)", "x + @"]:
            ttk.Button(
                examples,
                text=example,
                command=lambda value=example: self.load_example(value)
            ).pack(side="left", padx=3)

        buttons = tk.Frame(main, bg="#f1f5f9")
        buttons.pack(fill="x", pady=(0, 14))

        tk.Button(
            buttons,
            text="Validate Formula",
            command=self.validate,
            font=("Segoe UI", 11, "bold"),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            relief="flat",
            padx=18,
            pady=9,
            cursor="hand2"
        ).pack(side="left")

        ttk.Button(
            buttons,
            text="Clear",
            command=self.clear
        ).pack(side="left", padx=10)

        self.status = tk.Label(
            main,
            text="Enter a formula and click Validate Formula.",
            font=("Segoe UI", 10, "bold"),
            bg="#e2e8f0",
            fg="#334155",
            anchor="w",
            padx=12,
            pady=10
        )
        self.status.pack(fill="x", pady=(0, 12))

        output_frame = tk.Frame(main, bg="#f1f5f9")
        output_frame.pack(fill="both", expand=True)

        left = tk.Frame(output_frame, bg="#f1f5f9")
        left.pack(side="left", fill="both", expand=True, padx=(0, 6))

        right = tk.Frame(output_frame, bg="#f1f5f9")
        right.pack(side="left", fill="both", expand=True, padx=(6, 0))

        tk.Label(
            left,
            text="Validation Details",
            font=("Segoe UI", 11, "bold"),
            bg="#f1f5f9",
            fg="#172554"
        ).pack(anchor="w", pady=(0, 6))

        self.details = self.create_output(left)

        tk.Label(
            right,
            text="Abstract Syntax Tree (AST)",
            font=("Segoe UI", 11, "bold"),
            bg="#f1f5f9",
            fg="#172554"
        ).pack(anchor="w", pady=(0, 6))

        self.ast_output = self.create_output(right)

        footer = tk.Label(
            self.root,
            text="Compiler Design Mini Project",
            bg="#172554",
            fg="#cbd5e1",
            font=("Segoe UI", 9),
            pady=8
        )
        footer.pack(fill="x")

    def create_output(self, parent):
        frame = tk.Frame(parent)
        frame.pack(fill="both", expand=True)

        text = tk.Text(
            frame,
            wrap="word",
            font=("Consolas", 10),
            bg="#ffffff",
            fg="#1e293b",
            padx=10,
            pady=10,
            relief="solid",
            bd=1,
            state="disabled"
        )

        scrollbar = ttk.Scrollbar(
            frame,
            orient="vertical",
            command=text.yview
        )
        text.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        text.pack(side="left", fill="both", expand=True)

        return text

    def set_text(self, widget, content):
        widget.configure(state="normal")
        widget.delete("1.0", tk.END)
        widget.insert("1.0", content)
        widget.configure(state="disabled")

    def load_example(self, example):
        self.formula.delete(0, tk.END)
        self.formula.insert(0, example)
        self.validate()

    def validate(self):
        formula = self.formula.get().strip()

        self.set_text(self.details, "")
        self.set_text(self.ast_output, "")

        if not formula:
            self.status.config(
                text="Please enter a formula.",
                bg="#fef3c7",
                fg="#92400e"
            )
            return

        details = []

        # Stage 1: Lexical analysis
        try:
            tokens = tokenize(formula)
            details.append("LEXICAL ANALYSIS: Passed")
            details.append("Tokens generated successfully.")
        except (SyntaxError, ValueError) as error:
            details.append("LEXICAL ANALYSIS: Failed")
            details.append(str(error))
            self.show_invalid(details, "Lexical error")
            return

        # Stage 2: Syntax analysis
        try:
            parser = Parser(tokens)
            ast = parser.parse()
            details.append("")
            details.append("SYNTAX ANALYSIS: Passed")
            details.append("Formula follows the grammar.")
        except (SyntaxError, ValueError) as error:
            details.append("")
            details.append("SYNTAX ANALYSIS: Failed")
            details.append(str(error))
            self.show_invalid(details, "Syntax error")
            return

        # Stage 3: Semantic analysis
        try:
            analyzer = SemanticAnalyzer()
            analyzer.analyze(ast)
            details.append("")
            details.append("SEMANTIC ANALYSIS: Passed")
            details.append("Selected semantic checks passed.")
        except SemanticError as error:
            details.append("")
            details.append("SEMANTIC ANALYSIS: Failed")
            details.append(str(error))
            self.show_invalid(details, "Semantic error")
            return

        # Print AST into a string instead of the terminal
        ast_buffer = StringIO()
        with redirect_stdout(ast_buffer):
            print_ast(ast)

        self.set_text(self.details, "\n".join(details))
        self.set_text(self.ast_output, ast_buffer.getvalue())

        self.status.config(
            text="VALID FORMULA — All checks passed",
            bg="#dcfce7",
            fg="#166534"
        )

    def show_invalid(self, details, error_type):
        self.set_text(self.details, "\n".join(details))
        self.set_text(
            self.ast_output,
            "AST is not displayed because validation failed."
        )
        self.status.config(
            text=f"INVALID FORMULA — {error_type}",
            bg="#fee2e2",
            fg="#991b1b"
        )

    def clear(self):
        self.formula.delete(0, tk.END)
        self.set_text(self.details, "")
        self.set_text(self.ast_output, "")
        self.status.config(
            text="Enter a formula and click Validate Formula.",
            bg="#e2e8f0",
            fg="#334155"
        )
        self.formula.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    app = MathFormulaGUI(root)
    root.mainloop()
