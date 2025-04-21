#
# KimHong Poun
# 04/20/2025
# Capital Quiz Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
import random
def state_cap_dictionary():

        sc = {'Alabama':'Montgomery', 'Alaska':'Juneau',
                'Arizona':'Phoenix', 'Arkansas':'Little Rock',
                'California':'Sacramento', 'Colorado':'Denver',
                'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta',
                'Hawaii':'Honolulu', 'Idaho':'Boise',
                'Illinois':'Springfield', 'Indiana':'Indianapolis',
                'Iowa':'Des Moines', 'Kansas':'Topeka',
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
                'Maine':'Augusta', 'Maryland':'Annapolis',
                'Massachusetts':'Boston', 'Michigan':'Lansing',
                'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                'Missouri':'Jefferson City', 'Montana':'Helena',
                'Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord', 'New Jersey':'Trenton',
                'New Mexico':'Santa Fe', 'New York':'Albany',
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
                'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                'Rhode Island':'Providence', 'South Carolina':'Columbia',
                'South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin', 'Utah':'Salt Lake City',
                'Vermont':'Montpelier', 'Virginia':'Richmond',
                'Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}
        return sc

NUM_STATES = 5
def main():
    # Initialize dictionary
    state_caps = state_cap_dictionary()

    # Initial varibles to keep count of the number 
    # of correct and incorrect answer.
    correct = 0
    incorrect = 0

    # Quiz the user.
    for count in range (NUM_STATES):
        # Get a random entry from the dictionary
        state, capital = state_caps.popitem()

        # Quiz the user.
        print('What is the capital of ', state, '? ', end=' ')
        response = input()

        # Is the user correct?
        if response.lower() == capital.lower():
            correct += 1
            print('Correct!')
        else:
            incorrect += 1
            print('Incorrect!')

    # Display the results.
    print('Correct responses:', correct)
    print('Incorrect responses:', incorrect)

    # Local variables

    # Continue until user quits the game.

# Call the main function.
main()
