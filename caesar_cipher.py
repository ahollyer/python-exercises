#!/usr/bin/env python3

# caesar_cipher.py
# By Aspen
# Accepts a string and amount to shift, returns shifted string

# 6. Caesar Cipher

# Create a list of characters to use indices for shifting
## NOTE: 4/24/17 can use string instead of list:
## string.ascii_lowercase
CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Choose a string to translate
str = input("Enter a string to shift: ").lower()


# Determine the amount to shift
shift_key = int(input("How much do you want to shift? Enter an integer."))



# Create a function that accepts the string & shift key
def c_shift(str, shift_key):
    # Create an empty string to add shifted chars
    shifted_str = ""

    # Iterate over each character in the input string
    for char in str:

        # Don't shift spaces or punctuation; just add to shifted_str
        try:
            i = chars.index(char)
        except ValueError:
            shifted_str += char
            continue

        # Apply the shift key
        try:
            c = chars[i + shift_key]
        except IndexError:
            if i + shift_key < 0:
                c = chars[26 + (i + shift_key)]
            elif i + shift_key > 25:
                c = chars[i + shift_key - 26]

        # Append the shifted character to shifted_str
        shifted_str += c
    return shifted_str

print(str)
print("Shifted:", c_shift(str, shift_key))
print("Unshifted:", c_shift(c_shift(str, shift_key), -shift_key))

puzzle = "lbh zhfg hayrnea jung lbh unir yrnearq"
print("\nPuzzle:", puzzle + "\nDeciphered:", c_shift(puzzle, -13))
