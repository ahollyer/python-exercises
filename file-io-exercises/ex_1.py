# ex_1.py
# By Aspen
# INSTRUCTIONS: Write a program that prompts the user to enter a file name,
# reads the contents of the file, and prints it to the screen.

def read_my_file():
    print("\nThis program prints the contents of your file to the screen.")
    my_file = input('Enter the name of the file to print: ')

    with open(my_file, 'r') as fh:
        contents = fh.read()

    print(contents)

if __name__ == '__main__':
    read_my_file()
