#
# KimHong Poun
# 02/14/2025
# Bug Collector Programming Project
# COSC 1010
#
# Initialize variables for bugs and total number of bugs collected.
Total = 0
# Get number of bugs collected each day using a for loop.
for day in range (1, 8):
    print("Enter the bug collected in day", day)
    bugs = int(input())
    Total += bugs
# Display the total number of bugs collected.
print("You collected a total of",Total, "bug")