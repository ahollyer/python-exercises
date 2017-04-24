# bonus_challenge.py
# By Aspen

# INSTRUCTIONS: Given a histogram tally (one returned from either
# letter_histogram or word_histogram), print the top 3 words or letters.

import string

def word_histogram(text):
    stripped_text = text.translate(string.punctuation)
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

def top_3(histogram):
    # Generate list of words sorted by values in descending order
    sorted_dict = sorted(histogram, key=histogram.__getitem__, reverse=True)
    # To print top 3
    # print(sorted_dict[:3])
    return sorted_dict[:3]

if __name__ == '__main__':
    hist = word_histogram("Congress returns Tuesday from its spring\
    recess,facing yet another down-to-the-wire spate of deal-making\
    and a White House anxious to claim its first major legislative\
    win. On Friday night, the funding measure lawmakers approved\
    last year to keep the federal government running will expire.\
    The timing leaves members of the House and Senate just four\
    days to reach a new agreement to fund the government, or risk\
    a partial shutdown of federal agencies on Saturday — the 100th\
    day of Donald Trump's presidency.")

    top_3(hist)
