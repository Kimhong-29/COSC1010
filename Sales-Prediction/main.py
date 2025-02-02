#
# KimHong Poun
# 01/31/2025
# Sales Prediction Programming Project
# COSC 1010
#

# Variables to hold the sales total and the profit

# Get the amount of projected sales.

total_sales = float(input("Enter the projected sale: "))

# Calculate the projected profit.

profit = total_sales * 0.23

# Print the projected profit.

print(f"The profit is $", format(profit, ',.2f'))