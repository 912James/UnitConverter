
# GUI for the Unit converter application

import tkinter as tk
from tkinter import ttk
from converter import UnitConverter

class ConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter by Janies Soto")
        self.converter = UnitConverter()

        # Category selection
        tk.Label(root, text="Select Category:").grid(row=0, column=0, padx=5, pady=5)
        self.category_var = tk.StringVar()
        self.category_dropdown = ttk.Combobox(root, textvariable=self.category_var, values=self.converter.get_categories())
        self.category_dropdown.grid(row=0, column=1, padx=5, pady=5)
        self.category_dropdown.bind("<<ComboboxSelected>>", self.update_units)
        self.category_dropdown.set("distance")  # Default

        # Unit selection
        tk.Label(root, text="From:").grid(row=1, column=0, padx=5, pady=5)
        self.from_var = tk.StringVar()
        self.from_dropdown = ttk.Combobox(root, textvariable=self.from_var)
        self.from_dropdown.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="To:").grid(row=2, column=0, padx=5, pady=5)
        self.to_var = tk.StringVar()
        self.to_dropdown = ttk.Combobox(root, textvariable=self.to_var)
        self.to_dropdown.grid(row=2, column=1, padx=5, pady=5)

        # User input field
        tk.Label(root, text="Value:").grid(row=3, column=0, padx=5, pady=5)
        self.value_entry = tk.Entry(root)
        self.value_entry.grid(row=3, column=1, padx=5, pady=5)

        # Convert button
        tk.Button(root, text="Convert", command=self.convert).grid(row=4, column=1, pady=10)

        # Results label
        self.result_label = tk.Label(root, text="Result: ")
        self.result_label.grid(row=5, column=0, columnspan=2, pady=5)

        # Initial unit population
        self.update_units(None)

    def update_units(self, event):
        # Unit dropdowns based on selected category
        category = self.category_var.get()
        units = self.converter.get_units(category)
        self.from_dropdown["values"] = units
        self.to_dropdown["values"] = units
        self.from_var.set(units[0])  
        self.to_var.set(units[1] if len(units) > 1 else units[0])

    def convert(self):
        #Perform conversion and display result 
        try:
            value = float(self.value_entry.get())
            from_unit = self.from_var.get()
            to_unit = self.to_var.get()
            category = self.category_var.get()
            result = self.converter.convert(value, from_unit, to_unit, category)
            self.result_label.config(text=f"Result: {value} {from_unit} = {result:.5f} {to_unit}")
        except ValueError:
            self.result_label.config(text="Error: Please enter a valid number")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")