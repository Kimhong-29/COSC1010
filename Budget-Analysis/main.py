#
# KimHong Poun
# 02/15/2025
# Budget Analysis Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.
# Montly budget input
Budget_for_month = float(input("Enter this month budget: $"))

# Initialize variables

Total_Expense = 0
week = 1

# Get weekly Expense
while True:
    print(f"Enter expenses for week {week} (or enter 0 to finish):")
    Expense = float(input("$"))
    
    if Expense == 0:  # Sentinel value to stop the loop
        break
    
    Total_Expense += Expense
    week += 1

Difference = Budget_for_month - Total_Expense

# Checking if over budget or lower

if Difference > 0:
    print(f"You are under budget by ${Difference:.2f}")
elif Difference < 0:
    print(f"You are over budget by ${abs(Difference):.2f}")
else:
    print("You are exactly on budget.")