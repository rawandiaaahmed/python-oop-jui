#!/usr/bin/env python
# coding: utf-8

# In[7]:


import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
class Expense:
    def __init__(self, amount, category, description, date=None):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")
class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_total(self):
        return sum(exp.amount for exp in self.expenses)

class ExpenseTrackerApp:
    def __init__(self, root):
        self.manager = ExpenseManager()
        self.root = root
        self.root.title("Smart Expense Tracker")
        self.root.geometry("650x500")
        self.root.configure(bg="#f8f9fa")

        self.create_header()
        self.create_buttons()
        self.create_table()
        self.create_status_bar()

  
    def create_header(self):
        header = tk.Frame(self.root, bg="#2c3e50", height=60)
        header.pack(fill="x")

        title = tk.Label(
            header,
            text="Smart Expense Tracker",
            font=("Arial", 20, "bold"),
            fg="white",
            bg="#2c3e50",
        )
        title.pack(pady=10)

    def create_buttons(self):
        btn_frame = tk.Frame(self.root, bg="#f8f9fa")
        btn_frame.pack(pady=10)

        self.add_btn = tk.Button(
            btn_frame,
            text="Add Expense",
            font=("Arial", 12, "bold"),
            bg="#2980b9",
            fg="white",
            width=15,
            relief="flat",
            command=self.open_add_window,
        )
        self.add_btn.grid(row=0, column=0, padx=10)

        self.report_btn = tk.Button(
            btn_frame,
            text="Show Report",
            font=("Arial", 12, "bold"),
            bg="#2980b9",
            fg="white",
            width=15,
            relief="flat",
            command=self.show_report,
        )
        self.report_btn.grid(row=0, column=1, padx=10)

        self.clear_btn = tk.Button(
            btn_frame,
            text="Clear All",
            font=("Arial", 12, "bold"),
            bg="#2980b9",
            fg="white",
            width=15,
            relief="flat",
            command=self.clear_all,
        )
        self.clear_btn.grid(row=0, column=2, padx=10)

 
    def create_table(self):
        frame = tk.Frame(self.root, bg="#f8f9fa")
        frame.pack(fill="both", expand=True, padx=20, pady=10)

        columns = ("Amount", "Category", "Description", "Date")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 11, "bold"))
        style.configure("Treeview", font=("Arial", 10), rowheight=25)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=130)

        self.tree.pack(fill="both", expand=True)

  
    def create_status_bar(self):
        self.status_label = tk.Label(
            self.root, text="Total Expenses: 0 EGP", bg="#2c3e50", fg="white", font=("Arial", 12)
        )
        self.status_label.pack(fill="x", side="bottom")

 
    def open_add_window(self):
        add_win = tk.Toplevel(self.root)
        add_win.title("Add New Expense")
        add_win.geometry("350x350")
        add_win.configure(bg="#ecf0f1")

        tk.Label(add_win, text="Amount:", font=("Arial", 12, "bold"), bg="#ecf0f1").pack(pady=5)
        amount_entry = tk.Entry(add_win, font=("Arial", 12))
        amount_entry.pack(pady=5)

        tk.Label(add_win, text="Category:", font=("Arial", 12, "bold"), bg="#ecf0f1").pack(pady=5)
        category_entry = tk.Entry(add_win, font=("Arial", 12))
        category_entry.pack(pady=5)

        tk.Label(add_win, text="Description:", font=("Arial", 12, "bold"), bg="#ecf0f1").pack(pady=5)
        desc_entry = tk.Entry(add_win, font=("Arial", 12))
        desc_entry.pack(pady=5)

        def save_expense():
            try:
                amount = float(amount_entry.get())
                category = category_entry.get()
                desc = desc_entry.get()

                if not category or not desc:
                    messagebox.showwarning("Error", "All fields are required!")
                    return

                expense = Expense(amount, category, desc)
                self.manager.add_expense(expense)
                self.tree.insert(
                    "", "end",
                    values=(expense.amount, expense.category, expense.description, expense.date)
                )
                self.update_status()
                add_win.destroy()
            except ValueError:
                messagebox.showerror("Error", "Amount must be a number!")

        tk.Button(
            add_win, text="Save Expense", bg="#27ae60", fg="white",
            font=("Arial", 12, "bold"), width=15, relief="flat", command=save_expense
        ).pack(pady=20)

 
    def show_report(self):
        total = self.manager.get_total()
        messagebox.showinfo("Report", f"Your total expenses are: {total:.2f} EGP")

  
    def clear_all(self):
        self.manager.expenses.clear()
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.update_status()

   
    def update_status(self):
        total = self.manager.get_total()
        self.status_label.config(text=f"Total Expenses: {total:.2f} EGP")
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()


# In[ ]:





# In[ ]:




