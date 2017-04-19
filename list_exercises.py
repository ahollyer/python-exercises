# list-exercises.py
# By Aspen
# a collection of brief programming exercises on lists

import random

num_list = list(range(-5, 10))
random.shuffle(num_list)
print("The list of numbers is:", num_list)

# 1. Sum the Numbers
# Given a list of numbers, print their sum.
ex1_sum = 0
for num in num_list:
    ex1_sum += num
print("1. Sum the Numbers:", ex1_sum)

# 2. Largest Number
ex2_largest = 0
for num in num_list:
    if num > ex2_largest:
        ex2_largest = num
print("2. Largest Number:", ex2_largest)

# 3. Smallest Number
ex3_smallest = num_list[0]
for num in num_list:
    if num < ex3_smallest:
        ex3_smallest = num
print("3. Smallest Number:", ex3_smallest)

# 4. Even Numbers
print("4. Even Numbers:")
for num in num_list:
    if num % 2 == 0:
        print("\t", num)

# 5. Positive Numbers
print("5. Positive Numbers:")
for num in num_list:
    if num > 0:
        print("\t", num)

# 6. Positive Numbers II
ex6_list = []
for num in num_list:
    if num > 0:
        ex6_list.append(num)
print("6. List of Positive Numbers:", ex6_list)

# 7. Multiply a List
ex7_list = []
def multiply_list(list, factor):
    for num in list:
        ex7_list.append(num * factor)
    return ex7_list
print("7. Multiply a List:\n", multiply_list(num_list, 2))

# 8. Multiply Vectors
ex8_list1 = [2, 4, 5]
ex8_list2 = [2, 3, 6]
product = []
def multiply_vectors(a, b):
    for i in range(0, len(a)):
        product.append(a[i] * b[i])
    return product
print("8. Multiply Vectors:\n", multiply_vectors(ex8_list1, ex8_list2))

# 9. Matrix Addition
ex9_list1 = [[1, 3], [2, 4]]
ex9_list2 = [[5,2], [1, 0]]
ex9_sum = []
def add_matrices(a, b):
    # Iterate over list
    for i in range(0, len(a)):
        # Iterate over sub-list
        temp = []
        for j in range(0, len(a[i])):
            temp.append(a[i][j] + b[i][j])
        ex9_sum.append(temp)
    return ex9_sum
print("9. Matrix Addition:\n", add_matrices(ex9_list1, ex9_list2))

# 10. Matrix Addition II
# see above
print("10. Matrix Addition II: (see exercise 9)")

# 11. De-dup
ex11_original = [1, 2, 2, 3, 4, 5, 6, 4, 7, 5, 5]
ex11_deduped = []
def dedup(list):
    for num in ex11_original:
        if not num in ex11_deduped:
            ex11_deduped.append(num)
    return ex11_deduped
print("11. De-dup:\nOriginal List:", ex11_original, "\nDe-Duped List:", dedup(ex11_original))

# Bonus: Matrix Multiplication
bonus1 = [[2, -2], [5, 3]]
bonus2 = [[-1, 4], [7, -6]]
def multiply_matrices(a, b):
    product = []
    for i in range(len(a)):
        temp = []
        for j in range(len(a[i])):
            sum = 0
            for k in range(len(b)):
                sum += (a[i][k] * b[k][j])
            temp.append(sum)
        product.append(temp)
    return product
print("Bonus - Matrix Multiplication:", multiply_matrices(bonus1, bonus2))
