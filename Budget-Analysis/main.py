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

# Get weekly Expense
for week in range(1,5):
    print("Enter expenese in week ",week)
    Expense = float(input("$"))
    Total_Expense += Expense

Difference = Budget_for_month - Total_Expense

# Checking if over budget or lower

if Difference > 0:
    print(f"You are under budget by ${Difference:.2f}")
elif Difference < 0:
    print(f"You are over budget by ${abs(Difference):.2f}")
else:
    print("You are exactly on budget.")