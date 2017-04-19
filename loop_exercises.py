# loop_exercises.py
# By Aspen
# A collection of brief programming exercises with loops

# 1. 1 to 10
print("\n1. 1 to 10:")
for i in range(1, 11):
    print("\t", i)

# 2. n to m
print("\n2. n to m:")
start = int(input("Start from: "))
end = int(input("End on: "))
def count_loop(start, end):
    for i in range(start, end+1):
        print("\t", i)
count_loop(start, end)

# 3. Odd Numbers
print("\n3. Odd Numbers:")
for i in range(1, 10, 2):
    print("\t", i)

# 4. Print a Square
print("\n4. Print a Square:")
unit = "*"
side = 5
for i in range(0, side):
    print(unit * side)

# 5. Print a Square II
print("\n5. Print a Square II:")
side = int(input("How long is each side? Enter an integer: "))
for i in range(0, side):
    print(unit * side)

# 6. Print a Box
print("\n6. Print a Box:")
height = int(input("How tall is the box? Enter an integer: "))
width = int(input("How wide is the box? Enter an integer: "))
def print_box(w, h):
    print("*" * w)
    for i in range(0, (h-2)):
        print("*" + (" " * (w-2)) + "*")
    print("*" * w)
print_box(width, height)

# 7. Print a Triangle
(print("\n7. Print a Triangle:"))
print(" " * 3 + "*" * 1 + " " * 3)
print(" " * 2 + "*" * 3 + " " * 2)
print(" " * 1 + "*" * 5 + " " * 1)
print(" " * 0 + "*" * 7 + " " * 0)

# 8. Print a Triangle II
print("\n8. Print a Triangle II:")
height = int(input("What is the triangle's height? Enter an integer: "))
def print_triangle(h):
    num_stars = 1
    for i in range(0, h):
        print(" " * (h-i) + "*" * num_stars + " " * (h-i))
        num_stars += 2
print_triangle(height)
