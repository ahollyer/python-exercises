# hello2.py
# by Aspen Hollyer
# Asks for a name as input and prints the name in all caps as well as the number of characters in the name

def main():
    name = input("What is your name? ").upper()
    print("HELLO,", name)
    print("YOUR NAME HAS", len(name), "LETTERS IN IT! AWESOME!")

main()
