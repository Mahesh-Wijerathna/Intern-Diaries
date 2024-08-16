




import tkinter as tk
from tkinter import messagebox

def calculate_electricity_bill():
    try:
        previous_reading = float(entry_previous.get())
        current_reading = float(entry_current.get())
        
        units_used = current_reading - previous_reading
        
        if units_used < 30:
            rate = 1.5
        elif units_used < 90:
            rate = 2.5
        else:
            rate = 4.5
        
        bill_amount = units_used * rate
        
        label_result.config(text=f"Units Used: {units_used:.2f}\nTotal Bill: LKR {bill_amount:.2f}")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for the meter readings.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Set up the main application window
app = tk.Tk()
app.title("Electricity Bill Calculator")
app.geometry("350x250")  # Adjust the window size to 350x250 pixels

tk.Label(app, text="Previous Meter Reading:").pack(pady=10)
entry_previous = tk.Entry(app)
entry_previous.pack(pady=5)

tk.Label(app, text="Current Meter Reading:").pack(pady=10)
entry_current = tk.Entry(app)
entry_current.pack(pady=5)

tk.Button(app, text="Calculate Bill", command=calculate_electricity_bill).pack(pady=10)
label_result = tk.Label(app, text="")
label_result.pack(pady=5)

app.mainloop()
