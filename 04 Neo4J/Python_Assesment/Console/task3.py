
def calculate_marks():
    print("---- Marks Calculation ----")
    marks = []
    for i in range(1, 6):
        try:
            mark = float(input(f"Enter marks for student {i}: "))
            marks.append(mark)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return

    total_marks = sum(marks)
    average_marks = total_marks / 5

    print("\n---- Marks Summary ----")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")

# Call the function
calculate_marks()


