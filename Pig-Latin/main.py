#
# KimHong Poun
# 04/13/2025
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
def main():
    # Get a sentence from user
    english_sentence = input('Enter an English sentence: ')
    
    # Convert to Pig Latin and display result
    pig_latin = convert_to_pig_latin(english_sentence)
    print('Pig Latin:', pig_latin)

def convert_to_pig_latin(sentence):
    words = sentence.split()
    
    # Process each word
    pig_latin_words = []
    for word in words:
        if len(word) > 0:
            # Convert word to Pig Latin
            pig_word = convert_word(word)
            pig_latin_words.append(pig_word)
    
    return ' '.join(pig_latin_words)

def convert_word(word):
    if len(word) == 1:
        return word.upper() + 'AY'
    
    first_letter = word[0]
    rest_of_word = word[1:]
    return (rest_of_word + first_letter).upper() + 'AY'

# Call the main function
main()