# multiplication_table.py
# By Aspen
# Uses a loop to print the multiplication table for numbers 1-10.

print("\n9. Multiplication Table:")
for i in range(1, 11):
    print("Multiples of", str(i))
    for j in range(1, 11):
        print(str(i) + " * " + str(j) + " = " + str(i*j))
