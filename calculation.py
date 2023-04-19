import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("300x400")

        self.entry = tk.Entry(master, width=30, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_button(1, 0, 1)
        self.create_button(1, 1, 2)
        self.create_button(1, 2, 3)
        self.create_button(1, 3, "+")

        self.create_button(2, 0, 4)
        self.create_button(2, 1, 5)
        self.create_button(2, 2, 6)
        self.create_button(2, 3, "-")

        self.create_button(3, 0, 7)
        self.create_button(3, 1, 8)
        self.create_button(3, 2, 9)
        self.create_button(3, 3, "*")

        self.create_button(4, 0, ".")
        self.create_button(4, 1, 0)
        self.create_button(4, 2, "/")
        self.create_button(4, 3, "=")

        self.create_button(5, 0, "C")

    def create_button(self, row, col, text):
        button = tk.Button(self.master, text=text, width=7, height=2, command=lambda: self.button_click(text))
        button.grid(row=row, column=col, padx=5, pady=5)

    def button_click(self, text):
        if text == "C":
            self.entry.delete(0, tk.END)
        elif text == "=":
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        else:
            self.entry.insert(tk.END, text)

root = tk.Tk()
calc = Calculator(root)
root.mainloop()
