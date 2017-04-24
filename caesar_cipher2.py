#!/usr/bin/env python3

# caesar_cipher2.py

# Accepts a rotation amount and string, returns a string
# shifted by the rotation amount

import string
import sys

def caesar_cipher (rotation, text):
    answer = ""
    for t in text:
        t = t.lower()
    if t in string.ascii_lowercase:
        index = string.ascii_lowercase.index(t)
        index = index - rotation
        answer += string.ascii_lowercase[index]
    answer += t
    return answer

if __name__ == "__main__":
    rotation = int(sys.argv[1])
    text = sys.argv[2]
    answer = caesar_cipher(rotation, text)
    print('Answer: {}'.format(answer))
