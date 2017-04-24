#!/usr/bin/env

# phonebook.py
# By Aspen
# A command line program to manage a phone book.

def lookup_entry():
    print('lookup')
    return

def set_entry():
    print('set')
    return

def delete_entry():
    print('delete')
    return

def list_entries():
    print('list')
    return

def quit():
    print('quit')
    in_use = False

def use_phonebook():
    functions = {
        '1': lookup_entry(),
        '2': set_entry(),
        '3': delete_entry(),
        '4': list_entries(),
        '5': quit,
    }
    in_use = True

    while in_use:
        print('Electronic Phone Book\n\
        =====================\n\
        1. Look up an entry\n\
        2. Set an entry\n\
        3. Delete an entry\n\
        4. List all entries\n\
        5. Quit\n')

        try:
            ans = int(input("What do you want to do (1-5)? "))
        except ValueError:
            print("\nYour input must be a number.")

        functions.get(ans)


if __name__ == '__main__':
    use_phonebook()
