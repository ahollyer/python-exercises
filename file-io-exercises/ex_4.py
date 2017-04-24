# ex_4.py
# By Aspen
# INSTRUCTIONS: Write a program that takes a JSON file name as input and
# plots the X,Y data.

import json
import matplotlib.pyplot as p

def plot_data(source):
    with open(source, 'r') as fh:
        obj = json.load(fh)

    xs = []
    ys = []

    for i in obj['data']:
        xs.append(i[0])
        ys.append(i[1])

    p.plot(xs, ys)
    p.show()

if __name__ == '__main__':
    print("\nThis program accepts a .JSON file and plots the X,Y data.\n")
    my_file = input("Enter the file name: ")
    plot_data(my_file)
