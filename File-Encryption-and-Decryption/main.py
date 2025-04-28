#
# KimHong Poun
# 04/27/2025
# File Encryption and Decryption Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
# Encryption program
# encrypt.py

# Step 1: Create a dictionary for encryption
# decrypt.py

# Create the same dictionary and reverse it
codes = {
    'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '!', 'c': '8',
    'D': '^', 'd': '&', 'E': '*', 'e': '1', 'F': '(', 'f': ')',
    'G': '-', 'g': '_', 'H': '=', 'h': '+', 'I': '{', 'i': '}',
    'J': '[', 'j': ']', 'K': ':', 'k': ';', 'L': '<', 'l': '>',
    'M': '?', 'm': '/', 'N': '~', 'n': '`', 'O': '$', 'o': '.',
    'P': '|', 'p': ',', 'Q': '0', 'q': '2', 'R': '3', 'r': '4',
    'S': '5', 's': '6', 'T': '7', 't': '8', 'U': 'z', 'u': 'Z',
    'V': 'X', 'v': 'x', 'W': 'Y', 'w': 'y', 'X': 'V', 'x': 'v',
    'Y': 'W', 'y': 'w', 'Z': 'Q', 'z': 'q', ' ': ' '
}

# Reverse the dictionary for decoding
decode = {v: k for k, v in codes.items()}

# Open and decrypt the file
with open('encrypted.txt', 'r') as infile:
    encrypted_text = infile.read()
    decrypted_text = ''
    
    for char in encrypted_text:
        if char in decode:
            decrypted_text += decode[char]
        else:
            decrypted_text += char  # keep unknown characters the same

print("Decrypted text:")
print(decrypted_text)
