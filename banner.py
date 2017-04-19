# banner.py
# By Aspen
# Prints a string with a box around it. The box stretches to fit the size of the string

print("\n***\nINSTRUCTIONS: Enter text to create a banner with that message\n***\n")

message = input("What do you want your banner to say? ")

def print_banner(str):
    width = len(str) + 4
    print("*" * width)
    print("* " + str + " *")
    print("*" * width)
print_banner(message)
