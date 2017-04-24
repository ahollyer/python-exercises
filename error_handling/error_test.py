#!/usr/bin/env python3

def catch_error ():
    while True:
        try:
            x = int(input("Please enter an integer: "))

        except ValueError:
            raise ValueError("This is not an integer.")

        except MemoryError:
            print("Ran out of memory.")

        else:
            x += 13
            print(x)

        finally:
            print("Going around again!")

if __name__ == '__main__':
    catch_error()
