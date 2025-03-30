#
# KimHong Poun
# 03/30/2025
# Lottery Number Generator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import random

Max_Digits = 7 # Max number of digits 
Start = 0      # Start of the Random number range
End = 9        # End of the Random number range

# main function
def main():
    #Create a list
    number = [0] * 7

    # Populate the list with random numbers.
    for index in range (Max_Digits):
        number[index] = random.randint (Start, End)

    # Display the random numbers.
    print('Here are your lottery numbers: ')
    for index in range(Max_Digits):
        print(number[index], end=' ')
    print()

# Call the main function.
main()