#
# KimHong Poun
# 02/01/2025
# Sales Tax Programming Project
# COSC 1010
#

# Variable declarations
state_tax_rate = 0.05
country_tax_rate = 0.025
purchase_amount = 0.0
# Constants for the state and county tax rates

# Get the amount of the purchase.
purchase_amount = float(input("Enter the total purchase amount: $"))
# Calculate the state sales tax.
state_sales_tax = purchase_amount * state_tax_rate
# Calculate the county sales tax.
country_sales_tax = purchase_amount * country_tax_rate
# Calculate the total tax.
total_tax = state_sales_tax + country_sales_tax
# Calculate the total of the sale.
total_sales = purchase_amount + total_tax
# Print information about the sale.
print(f"State sales tax = ${state_sales_tax:.2f}")
print(f"Coutry sales tax = ${country_sales_tax:.2f}")
print(f"Total sales tax = ${total_tax:.2f}")
print(f"Total sales = ${total_sales:.2f}")