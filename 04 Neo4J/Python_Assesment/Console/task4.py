def calculate_electricity_bill():
    print("\nElectricity Bill Calculator")
    print("----------------------------")
    
    try:
        previous_reading = float(input("Enter the Previous Meter Reading: "))
        current_reading = float(input("Enter the Current Meter Reading: "))
        
        units_used = current_reading - previous_reading
        
        if units_used < 30:
            rate = 1.5
        elif units_used < 90:
            rate = 2.5
        else:
            rate = 4.5
        
        bill_amount = units_used * rate
        
        print("\nElectricity Bill Calculation:")
        print(f"Units Used: {units_used:.2f}")
        print(f"Rate per Unit: LKR {rate}")
        print(f"Total Bill Amount: LKR {bill_amount:.2f}")
    
    except ValueError:
        print("Invalid input! Please enter valid numbers for the meter readings.")
    except Exception as e:
        print(f"An error occurred: {e}")

calculate_electricity_bill()


