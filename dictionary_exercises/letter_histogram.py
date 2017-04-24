# letter_histogram.py
# By Aspen

# INSTRUCTIONS: Write a histogram function that takes a word as
# input and returns a dictionary containing the tally of how
# many times each letter of the alphabet was used in the word.

def letter_histogram (word):
    histogram = {}
    for char in word:
        if char in histogram:
            histogram[char] += 1
        else:
            histogram[char] = 1
    return histogram


if __name__ == '__main__':
    ans = input("Feed me a string, and I'll count the characters: ")
    ans = letter_histogram(ans)
    print(ans)
