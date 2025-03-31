import os
import tkinter as tk
from tkinter import messagebox

TODO_FILE = "todo_list.txt"

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")
        self.root.geometry("600x400")

        # Load tasks
        self.tasks = self.load_tasks()

        # Left frame for input area
        self.left_frame = tk.Frame(root)
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Task addition area
        tk.Label(self.left_frame, text="New Task:").pack()
        self.task_entry = tk.Entry(self.left_frame, width=30)
        self.task_entry.pack(pady=5)
        
        tk.Button(self.left_frame, text="Add Task", command=self.add_task).pack(pady=5)

        # Delete task input
        tk.Label(self.left_frame, text="Task Number to Delete:").pack(pady=5)
        self.delete_entry = tk.Entry(self.left_frame, width=10)
        self.delete_entry.pack(pady=5)
        
        tk.Button(self.left_frame, text="Delete Task", command=self.delete_task).pack(pady=5)

        tk.Button(self.left_frame, text="Quit", command=self.quit_app).pack(pady=20)

        # Right frame for list display
        self.right_frame = tk.Frame(root)
        self.right_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        tk.Label(self.right_frame, text="Your Todo List").pack()
        self.task_listbox = tk.Listbox(self.right_frame, width=40, height=20)
        self.task_listbox.pack(fill=tk.BOTH, expand=True)
        
        # Initial list update
        self.update_task_list()

    def load_tasks(self):
        if os.path.exists(TODO_FILE):
            with open(TODO_FILE, "r", encoding="utf-8") as file:
                return [line.strip() for line in file.readlines()]
        return []

    def save_tasks(self):
        with open(TODO_FILE, "w", encoding="utf-8") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        if not self.tasks:
            self.task_listbox.insert(tk.END, "No tasks yet. Taking it easy?")
        else:
            for i, task in enumerate(self.tasks, 1):
                self.task_listbox.insert(tk.END, f"{i}. {task}")

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.save_tasks()
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Added '{task}'. Let’s tackle it together!")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            num = int(self.delete_entry.get()) - 1
            if 0 <= num < len(self.tasks):
                removed = self.tasks.pop(num)
                self.save_tasks()
                self.update_task_list()
                self.delete_entry.delete(0, tk.END)
                messagebox.showinfo("Success", f"Deleted '{removed}'. Nice work!")
            else:
                messagebox.showerror("Error", "That number doesn’t exist. Tired eyes?")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def quit_app(self):
        messagebox.showinfo("Goodbye", "See you later! Good job today!")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()