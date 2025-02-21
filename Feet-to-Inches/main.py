#
# KimHong Poun
# 02/21/2025
# Feet to Inches Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.
# Initialize variables
Inches_Per_Foot =12 

#main function 
def main():
    # Get a number of feet from the user.
    feet = int(input("Enter a number of feet: "))

    # Convert that to inches
    print(feet, "equals", feet_to_inches(feet), "inches.")

# The feat_to_inches function converts feet to inches.
def feet_to_inches(feet): 
    return feet * Inches_Per_Foot

# Call the main function.
main()
