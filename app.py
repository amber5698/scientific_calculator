import tkinter as tk
from tkinter import messagebox
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("400x600")
        self.resizable(0, 0)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry field
        entry = tk.Entry(self, textvariable=self.input_text, font=('Arial', 24), bd=10, insertwidth=4, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sin', 'cos', 'tan', 'sqrt',
            '(', ')', '^', 'C'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(self, text=button, padx=20, pady=20, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
                self.input_text.set("")
        elif char == 'C':
            self.expression = ""
            self.input_text.set("")
        elif char in ['sin', 'cos', 'tan', 'sqrt']:
            if char == 'sqrt':
                result = math.sqrt(float(self.input_text.get()))
                self.input_text.set(result)
                self.expression = str(result)
            else:
                angle = float(self.input_text.get())
                if char == 'sin':
                    result = math.sin(math.radians(angle))
                elif char == 'cos':
                    result = math.cos(math.radians(angle))
                elif char == 'tan':
                    result = math.tan(math.radians(angle))
                self.input_text.set(result)
                self.expression = str(result)
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
