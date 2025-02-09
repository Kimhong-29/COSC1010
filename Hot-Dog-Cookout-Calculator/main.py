# Name: KimHong Poun
# Date: 02/09/2025
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#
# This program calculates the number of hot dog and bun packages needed for a cookout,
# as well as the number of leftovers.

# Variables
Num_of_people = 0
HotDog_per_person = 0
HotDog_package = 0
Bun_package = 0
Total_Hotdog = 0
Leftover_Bun = 0
Leftover_Hotdog = 0

# Get number of people
Num_of_people = int(input("Enter the number of people attending the cookout: "))

# Get number of hot dogs per person
HotDog_per_person = int(input("Enter the number of hot dogs each person will be given: "))

# Calculate the total number of hot dogs needed
Total_Hotdog = Num_of_people * HotDog_per_person

# Calculate the number of hot dog packages (10 hot dogs per package)
HotDog_package = Total_Hotdog // 10
if Total_Hotdog % 10 != 0: 
    HotDog_package += 1

# Calculate the number of bun packages (8 buns per package)
Bun_package = Total_Hotdog // 8
if Total_Hotdog % 8 != 0:  
    Bun_package += 1

# Calculate leftovers
Leftover_Hotdog = (HotDog_package * 10) - Total_Hotdog
Leftover_Bun = (Bun_package * 8) - Total_Hotdog

# Print out results
print(f"The minimum number of packages of hot dogs required: {HotDog_package}")
print(f"The minimum number of packages of hot dog buns required: {Bun_package}")
print(f"The number of hot dogs that will be left over: {Leftover_Hotdog}")
print(f"The number of hot dog buns that will be left over: {Leftover_Bun}")