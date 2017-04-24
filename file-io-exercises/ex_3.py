# ex_3.py
# By Aspen
# INSTRUCTIONS: Write a program that prompts the user to enter a file name,
# then prints the letter histogram and the word histogram of the file.

import histograms as h

def print_histograms(file):
    with open(file, 'r') as fh:
        content = fh.read()

    letter_hist_dict = h.letter_histogram(content)
    print("Histogram of Characters:")
    for key, val in letter_hist_dict.items():
        print("{}: {}".format(key, val))

    word_hist_dict = h.word_histogram(content)
    print("Histogram of Words:")
    for key, val in word_hist_dict.items():
        print("{}: {}".format(key, val))

if __name__ == '__main__':
    ans = input('Enter the file name: ')
    print_histograms(ans)
