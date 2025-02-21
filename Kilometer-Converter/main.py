#
# KimHong Poun
# 02/21/2025
# Kilometer Converter Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
# Initialize variables
Conversion_Factor = 0.6214

def main():
    # Get the distance in kilometers.
    kilometers = float(input("Enter a distance in kilometers: "))

    # Display the distace converted to miles.
    show_miles(kilometers)

def show_miles (km):
    #Calculate miles.
    miles = km * Conversion_Factor

    #Display the miles.
    print(f"{km} kilometers equals {miles:.2f} miles.")

# Call the main function
main()