def calculate_net_salary():
    print("Welcome to the Net Salary Calculator")
    print("------------------------------------")
    
    try:
        basic_salary = float(input("Enter the Basic Salary: "))
        
        if basic_salary < 15000:
            bonus = 0.1 * basic_salary
        elif 15000 <= basic_salary <= 25000:
            bonus = 0.15 * basic_salary
        else:
            bonus = 0.2 * basic_salary
            
        net_salary = basic_salary + bonus
        
        print("\nNet Salary Calculation:")
        print(f"Basic Salary: LKR {basic_salary:.2f}")
        print(f"Bonus Amount: LKR {bonus:.2f}")
        print(f"Net Salary: LKR {net_salary:.2f}")
    
    except ValueError:
        print("Invalid input! Please enter a valid number for the salary.")

calculate_net_salary()

