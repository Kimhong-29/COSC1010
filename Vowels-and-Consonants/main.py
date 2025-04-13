#
# KimHong Poun
# 04/13/2025
# Vowels and Consonants Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
# main function
def main():
    # Get a String from user.
    user_str = input('Enter a string of characters: ')

    # Report the vowels and consonants.
    print('That string has', num_vowels(user_str), 'vowels and', num_consonants(user_str), 'consonants.')

# The num_vowels function returns the number of vowels in the string.
def num_vowels(s):
    # Make a list containing the vowels.
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Initialize an accumulator.
    v_count = 0

    # Count the vowels in s.
    for ch in s:
        if ch.lower() in vowels:
            v_count += 1

    # Return the vowel count.
    return v_count

# The num_consonants function returns the number of consonants in the string.
def num_consonants(s):
    # Make a list containing the vowels.
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Initialize an accumulator.
    c_count = 0

    # Count the consonants in s.
    for ch in s:
        if ch.isalpha() and ch.lower() not in vowels:
            c_count += 1

    # Return the consonant count.
    return c_count

# Call the main function.
main()