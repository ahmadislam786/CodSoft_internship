#TASK-1 TO DO LIST WITH GUI APPLICATION

import tkinter as tk
from tkinter import messagebox
import pandas as pd
class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List Application")

        self.tasks = []
        self.task_var = tk.StringVar()

        self.task_entry = tk.Entry(master, textvariable=self.task_var, width=50)
        self.task_entry.grid(row=0, column=0, padx=12, pady=12, ipady=5)  
        self.task_entry.configure(bg='lightblue', fg='black') 

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=12, pady=12)
        self.add_button.configure(bg='green', fg='white')  

        self.task_listbox = tk.Listbox(master, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=12, pady=12)
        self.task_listbox.configure(bg='lightgrey', fg='black', selectbackground='green') 

        self.mark_completed_button = tk.Button(master, text="Mark Completed", command=self.mark_completed)
        self.mark_completed_button.grid(row=2, column=0, columnspan=2, pady=12)
        self.mark_completed_button.configure(bg='blue', fg='white')  

        self.show_list_button = tk.Button(master, text="Show To-Do List", command=self.show_tasks)
        self.show_list_button.grid(row=3, column=0, columnspan=2, pady=12)
        self.show_list_button.configure(bg='purple', fg='white')  

        self.quit_button = tk.Button(master, text="Exit", command=self.master.destroy)
        self.quit_button.grid(row=4, column=0, columnspan=2, pady=12)
        self.quit_button.configure(bg='red', fg='white')  

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.task_listbox.insert(tk.END, task)
            self.task_var.set("")
        else:
            messagebox.showwarning("Error", "Please enter a task.")

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["completed"] = True
            self.task_listbox.itemconfig(index, {'bg': 'green', 'fg': 'black'})
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def show_tasks(self):
        if not self.tasks:
            messagebox.showinfo("To-Do List", "No tasks in the list.")
        else:
            tasks_str = "To-Do List:\n"
            for index, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Not Completed"
                tasks_str += f'{index + 1}. {task["task"]} - {status}\n'

            messagebox.showinfo("To-Do List", tasks_str)

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.configure(bg='light grey')  
    root.mainloop()

if __name__ == "__main__":
    main()
