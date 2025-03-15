#
# KimHong Poun
# 03/15/2025
# Average of Numbers Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
myfile = open('numbers.txt', 'r')

# Initialize variables for sum and count.
total_sum = 0
count = 0

# Read and display the file's contents.
for line in myfile:
    number = int(line)
    total_sum += number
    count += 1
    average = total_sum / count

# Close the file.
myfile.close()

# Display the average.
print(f"The average of the numbers is: {average}")