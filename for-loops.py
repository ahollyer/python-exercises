# for-loops.py
# Aspen Hollyer

# MITx 6.001x for loop practice.

# Convert the following into code that uses a for loop.
# prints 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints "Goodbye!"

for i in range(2, 11, 2):
    print(i)
print("Goodbye!")


# Convert the following code into code that uses a for loop.
# prints "Hello!"
# prints 10
# prints 8
# prints 6
# prints 4
# prints 2

print("Hello!")
for i in range(10, 1, -2):
    print(i)

for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!')
