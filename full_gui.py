import tkinter as tk
from converter import CurrencyConverter


class CurrencyCalculatorApp:
    """Class to manage the GUI."""

    def __init__(self):
        """Start the app with default settings."""
        self.converter = CurrencyConverter()
        self.selected_currency = "MXN"
        self.mode = "converter"  # Start in converter mode

        # Starting GUI
        self.root = tk.Tk()
        self.root.title("Calculator & Currency Converter")

        self.create_widgets()

    def create_widgets(self):
        """Set up all GUI elements"""
        # Entry field
        self.entry = tk.Entry(self.root, width=40, justify="right", font=("Arial", 18), state="normal")
        self.entry.grid(row=0, column=0, columnspan=4, pady=15)

        # Instruction label
        self.instruction_label = tk.Label(
            self.root,
            text="Please select a currency, enter USD, and press Convert!",
            font=("Arial", 12),
            fg="blue",
        )
        self.instruction_label.grid(row=1, column=0, columnspan=4, pady=5)

        # Mode label
        self.mode_label = tk.Label(self.root, text="You are using the Converter", font=("Arial", 14))
        self.mode_label.grid(row=2, column=0, columnspan=4, pady=5)

        # Buttons
        self.create_buttons()

    def create_buttons(self):
        """Set up calculator and converter buttons"""
        # Calculator buttons
        buttons = [
            "7", "8", "9", "C",
            "4", "5", "6", "/",
            "1", "2", "3", "*",
            ".", "0", "=", "+",
            "-", "(", ")", "Convert"
        ]

        row_val = 3
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(self.root, text=button, width=10, height=3, font=("Arial", 14), command=action).grid(
                row=row_val, column=col_val, padx=5, pady=5
            )
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Toggle Mode button
        tk.Button(
            self.root,
            text="Switch Mode",
            width=20,
            height=3,
            font=("Arial", 14),
            command=self.toggle_mode,
        ).grid(row=row_val + 1, column=0, columnspan=4, padx=5, pady=5)

        # Currency buttons
        self.currency_buttons = []
        currencies = ["MXN", "CAD", "JPY", "EUR"]
        for i, currency in enumerate(currencies):
            button = tk.Button(
                self.root,
                text=currency,
                width=12,
                height=3,
                font=("Arial", 14),
                bg="green" if currency == "MXN" else "SystemButtonFace",
                fg="white" if currency == "MXN" else "black",
                command=lambda x=currency: self.set_currency(x),
            )
            button.grid(row=row_val + 2, column=i % 4, padx=5, pady=5)
            self.currency_buttons.append(button)

    def set_currency(self, currency: str):
        """Set the selected currency."""
        if self.mode == "converter":
            self.selected_currency = currency
            for button in self.currency_buttons:
                if button["text"] == currency:
                    button.config(bg="green", fg="white")
                else:
                    button.config(bg="SystemButtonFace", fg="black")
        else:
            self.update_entry("Switch to Converter mode to change currencies!")

    def toggle_mode(self):
        """Switch between calculator and converter modes."""
        self.entry.delete(0, tk.END)
        if self.mode == "converter":
            self.mode = "calculator"
            self.mode_label.config(text="You are using the Calculator", fg="black")
            self.instruction_label.config(text="Enter a calculation and press =")
        else:
            self.mode = "converter"
            self.mode_label.config(text="You are using the Converter", fg="green")
            self.instruction_label.config(
                text="Please select a currency, enter USD, and press Convert!"
            )

    def on_button_click(self, value: str):
        """Handle button clicks."""
        if self.mode == "calculator":
            if value == "C":  # Clear the entry field
                self.entry.delete(0, tk.END)
            elif value == "=":  # Evaluate the expression
                try:
                    expression = self.entry.get()
                    result = eval(expression)  # Evaluate the mathematical expression
                    self.entry.delete(0, tk.END)
                    self.entry.insert(tk.END, str(result))
                except Exception:
                    self.entry.delete(0, tk.END)
                    self.entry.insert(tk.END, "Error")
            else:  # Append the clicked button's value to the entry field
                self.entry.insert(tk.END, value)

        elif self.mode == "converter":
            if value.isdigit() or value == ".":  # Allow numbers and decimal point
                self.entry.insert(tk.END, value)
            elif value == "C":  # Clear the entry field
                self.entry.delete(0, tk.END)
            elif value == "Convert":  # Trigger currency conversion
                self.convert()
            else:
                self.update_entry("Switch to Calculator mode for operations!")

    def convert(self):
        """Convert USD to the selected currency"""
        try:
            amount = self.converter.validate_amount(self.entry.get())
            converted = self.converter.convert(amount, self.selected_currency)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, f"{amount} USD = {converted:.2f} {self.selected_currency}")
        except ValueError as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(e))

    def update_entry(self, message: str):
        """Update the entry field with a message."""
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, message)

    def run(self):
        """Run the app."""
        self.root.mainloop()

