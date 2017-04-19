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
