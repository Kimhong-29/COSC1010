#
# KimHong Poun
# 02/09/2025
# Areas of Rectangles Programming Project
# COSC 1010
#
# Local variables
Lenght1 = 0
Width1 = 0
Lenght2 = 0
Width2 = 0
Area1 = 0
Area2 = 0
# Get length A
Lenght1 = int(input("Enter the lenght of rectangle 1: "))
# Get width A
Width1 = int(input("Enter the width of rectangle 1: "))
# Get length B
Lenght2 = int(input("Enter the lenght of rectangle 2: "))
# Get width B
Width2 = int(input("Enter the width of rectangle 2: "))
# Calculate area A
Area1 = Lenght1 * Width1
# Calculate area B
Area2 = Lenght2 * Width2 
# Print area comparison using if-elif-else statements
if Area1 > Area2:
    print("Rectangle 1 has the greather area.")
elif Area2 > Area1:
    print("Rectangle 2 has the greather area.")   
else:
    print("Both have the save area.")