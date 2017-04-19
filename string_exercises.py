# string_exercises.py
# By Aspen
# A collection of basic exercises on string_exercises

str = "doubt kills more dreams than failure ever will"
print("\nInitial string:")
print(str, "\n")

# 1. Uppercase a string
print("\n1. Uppercase a string:")
print(str.upper(), "\n")

# 2. Capitalize a string
print("\n2. Capitalize a string:")
print(str.capitalize(), "\n")

# 3. Reverse a string
print("\n3. Reverse a string:")
def reverse_str(message):
    listified = list(message)
    listified.reverse()
    new_string = "".join(listified)
    return new_string
print(reverse_str(str))

# 4. Leetspeak
print("\n4. Translate to Leetspeak:")
def leetspeak(str):
    translation_key = { 'A' : '4',
                        'E' : '3',
                        'G' : '6',
                        'I' : '1',
                        'O' : '0',
                        'S' : '5',
                        'T' : '7' }
    str = str.upper()
    translated = ""
    for char in str:
        if char in translation_key:
            translated += translation_key[char]
        else:
            translated += char
    return translated
print(leetspeak(str), "\n")

# 5. Long-long vowels
print("\n5. Long-long vowels:")
def long_vowels(str):
    listified = list(str)
    for i in range(1, len(listified)):
        if listified[i] == listified[i-1]:
            if listified[i] == 'e' or listified[i] == 'o':
                listified.insert(i, (listified[i] * 3))
    translated_str = "".join(listified)
    return translated_str
print("Normal: A good man feels happy.")
print(long_vowels("Long-long vowels: A good man feels happy."), "\n")
