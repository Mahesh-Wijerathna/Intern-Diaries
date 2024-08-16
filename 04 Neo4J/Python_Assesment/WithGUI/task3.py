





import tkinter as tk
from tkinter import messagebox

def calculate_marks():
    try:
        marks = [float(entry.get()) for entry in entries]
        total_marks = sum(marks)
        average_marks = total_marks / len(marks)
        
        label_result.config(text=f"Total Marks: {total_marks}\nAverage Marks: {average_marks:.2f}")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all marks.")

# Set up the main application window
app = tk.Tk()
app.title("Marks Calculator")
app.geometry("300x400")  # Adjust the window size to 300x400 pixels

entries = []
for i in range(5):
    tk.Label(app, text=f"Enter marks for Student {i + 1}:").pack(pady=5)
    entry = tk.Entry(app)
    entry.pack(pady=5)
    entries.append(entry)

tk.Button(app, text="Calculate Marks", command=calculate_marks).pack(pady=10)
label_result = tk.Label(app, text="")
label_result.pack(pady=5)

app.mainloop()
