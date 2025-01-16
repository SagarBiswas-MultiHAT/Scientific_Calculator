import tkinter as tk
import math

class ScientificCalculator(tk.Tk):
    def __init__(self): # __init__ method is a special method in Python classes that is automatically called when a new object of the class is created.
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("400x500")
        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Entry widget for displaying the result
        entry = tk.Entry(self, textvariable=self.result_var, font=('Arial', 18), bd=10, relief=tk.GROOVE, justify=tk.RIGHT)
        entry.grid(row=0, column=0, columnspan=5, pady=10, padx=10, sticky='nsew')

        # List of buttons to be displayed in the calculator
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', '+', '=',
            'sin', 'cos', 'tan', 'sqrt',
            '^', '%', 'C', '⌫'
        ]

        # Create buttons and place them in the grid
        row_val, col_val = 1, 0
        for button in buttons:
            tk.Button(self, text=button, padx=20, pady=20, font=('Arial', 12), command=lambda btn=button: self.on_button_click(btn)).grid(row=row_val, column=col_val, padx=5, pady=5, sticky='nsew') # command=lambda btn=button: self.on_button_click(btn) is used to pass the button text to the on_button_click method. grid() is used to place the button in the grid layout.
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Make the grid responsive by configuring row and column weights
        for i in range(1, 6):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button): # self is a reference to the current instance of the class, and button. The on_button_click method is called when a button is clicked in the calculator.
        current_value = self.result_var.get() # Get the current value displayed in the calculator

        # Handle different button presses
        if button == '=':
            try:
                result = eval(current_value) # eval() function evaluates the expression passed to it and returns the result.
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        elif button == 'C':
            self.result_var.set('')  # Clear the display
        elif button == '⌫':
            # Remove last character from current value
            self.result_var.set(current_value[:-1])
        elif button == 'sqrt':
            try:
                # Compute the square root of the current value
                self.result_var.set(math.sqrt(float(current_value)))
            except ValueError:
                self.result_var.set("Error")
        elif button == '^':
            # Append the power operator for exponentiation
            self.result_var.set(current_value + '**')
        elif button in ('sin', 'cos', 'tan'):
            try:
                # Calculate trigonometric functions (in radians)
                angle = float(current_value)
                if button == 'sin':
                    result = math.sin(math.radians(angle))
                elif button == 'cos':
                    result = math.cos(math.radians(angle))
                elif button == 'tan':
                    result = math.tan(math.radians(angle))
                self.result_var.set(result)
            except ValueError:
                self.result_var.set("Error")
        else:
            # Append the pressed button to the current value
            self.result_var.set(current_value + str(button))


if __name__ == "__main__":
    app = ScientificCalculator()
    app.mainloop()
