# triangle_numbers.py
# By Aspen
# A program that prints the first 100 triangle numbers.

# What is a triangle number? See:
# https://www.mathsisfun.com/algebra/triangular-numbers.html

# Recursive solution
def print_triangle_nums(n):
    if n == 0:
        print("Done!")
    else:
        num = n * (n+1) / 2
        print(num)
        print_triangle_nums(n-1)
print_triangle_nums(100)

# For loop
def print_triangle_nums2(p):
    for i in range(1, p+1):
        num = i * (i+1) / 2
        print(num)
    print("Done!")
print_triangle_nums2(100)
