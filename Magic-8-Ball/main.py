#
# KimHong Poun
# 04/06/2025
# Magic 8 Ball Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
import random

def main():
    # Open and read responses from file exactly as you specified
    myfile = open('8_ball_responses.txt', 'r')
    responses = [line.strip() for line in myfile if line.strip()]
    myfile.close()

    print("Welcome to the Magic 8 Ball!")
    print("Ask me a yes/no question and I'll reveal your fortune...")
    print("(Enter 'quit' to exit)\n")

    while True:
        question = input("What is your question? ").strip()
        
        if question.lower() == 'quit':
            print("\nGoodbye! May your fortunes be favorable.")
            break
        
        if not question.endswith('?'):
            print("Please ask a proper question (end with a '?').")
            continue
        
        # Get random response using the same approach as your lottery example
        random_index = random.randint(0, len(responses) - 1) 
        print(f"\nMagic 8 Ball says: {responses[random_index]}\n")

main()