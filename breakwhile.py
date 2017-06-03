# breakwhile.py
# Aspen Hollyer

# MITx 6.001x Practice problems for understanding while loops

# Practice using break statement
num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')


# Convert the following into code that uses a while loop.
# print 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints Goodbye!

num = 0
while num < 10:
    num += 2
    print(num)
print('Goodbye!')

# Write a while loop that sums the values 1 through end, inclusive. end is a
# variable that we define for you. So, for example, if we define end to be 6,
# your code should print out the result: 21.

end = 6
num = 1
total = 0
while num <= end:
    total += num
    num += 1
print(total)
