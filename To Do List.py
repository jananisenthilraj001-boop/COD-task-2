import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task!")

# Function to delete a task
def delete_task():
    try:
        selected_task = task_list.curselection()
        task_list.delete(selected_task)
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Heading
heading = tk.Label(root, text="TO-DO LIST", font=("Arial", 16, "bold"))
heading.pack(pady=10)

# Entry box
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Add button
add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

# Listbox
task_list = tk.Listbox(root, width=40, height=10)
task_list.pack(pady=10)

# Delete button
delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)

# Run application
root.mainloop()
