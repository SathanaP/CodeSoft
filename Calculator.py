import tkinter as tk
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
def clear():
    entry.delete(0, tk.END)
root = tk.Tk()
root.title("Calculator")
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=evaluate)
    elif text == "C":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=clear)
    else:
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=lambda value=text: button_click(value))
    button.grid(row=row, column=col)
root.mainloop()
