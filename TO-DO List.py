import tkinter as tk
from tkinter import messagebox
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete!")
def clear_all():
    task_listbox.delete(0, tk.END)
root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", width=15, command=clear_all)
clear_button.pack(pady=5)

root.mainloop()
