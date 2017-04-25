# bonus_challenge.py
# By Aspen
# INSTRUCTIONS: Write a program that writes to an in-memory file and keeps
# track of how many characters/bytes were added and prints that information
# to the screen. Continue adding characters until your program dies.

# 1. At what count did your computer crash?

# 2. What kind of error did you get?

# 3. Did your program crash earlier or later than expected? Why do you think?

def crash():
    fh = open('crash.txt', 'w')
    counter = 0
    while True:
        fh.write('c' * (10 ** counter))
        counter += 10 ** counter
        print('Characters Written:', counter)


if __name__ == '__main__':
    crash()
