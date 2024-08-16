


import tkinter as tk
from tkinter import messagebox

def calculate_net_salary():
    try:
        basic_salary = float(entry_basic_salary.get())
        
        if basic_salary < 15000:
            bonus = 0.1 * basic_salary
        elif 15000 <= basic_salary <= 25000:
            bonus = 0.15 * basic_salary
        else:
            bonus = 0.2 * basic_salary
            
        net_salary = basic_salary + bonus
        
        label_result.config(text=f"Net Salary: LKR {net_salary:.2f}")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for the salary.")

# Set up the main application window
app = tk.Tk()
app.title("Net Salary Calculator")
app.geometry("300x200")  # Adjust the window size to 300x200 pixels

# Create and place widgets
tk.Label(app, text="Enter Basic Salary:").pack(pady=10)
entry_basic_salary = tk.Entry(app)
entry_basic_salary.pack(pady=5)

tk.Button(app, text="Calculate Net Salary", command=calculate_net_salary).pack(pady=10)
label_result = tk.Label(app, text="")
label_result.pack(pady=5)

app.mainloop()
