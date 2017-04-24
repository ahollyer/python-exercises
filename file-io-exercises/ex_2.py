# ex_2.py
# By Aspen
# INSTRUCTIONS: Write a program that prompts the user to enter a file name,
# prompts the user to enter content, and saves the content to the file.

def write_my_file():
    print("\nThis program accepts a file name and content, then creates\
    the file for you.\n")

    name = input("What should we call the file? ")
    content = input("What should we put in the file? ")

    with open(name, 'w') as fh:
        fh.write(content)

    print('\nDone! Here are the contents of', name + ":\n")
    with open(name, 'r') as fh:
        content = fh.read()

    print(content)

if __name__ == '__main__':
    write_my_file()
