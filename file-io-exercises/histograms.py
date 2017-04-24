# histograms.py
# By Aspen
# histogram module for ex_3.py

import string

def letter_histogram (word):
    histogram = {}
    for char in word:
        if char in histogram:
            histogram[char] += 1
        else:
            histogram[char] = 1
    return histogram


def word_histogram(text):
    stripped_text = text.translate(string.punctuation)
    print(stripped_text)
    histogram = {}
    for word in stripped_text.lower().split():
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    # To print histogram
    # for key, value in histogram.items():
    #    print(key + ":", value)
    return histogram

if __name__ == '__main__':
    ans = input("Feed me a string, and I'll count the characters: ")
    ans = letter_histogram(ans)
    print(ans)
