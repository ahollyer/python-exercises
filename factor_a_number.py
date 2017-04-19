# factor_a_number.py
# By Aspen
# Accepts an integer and prints its factors in ascending order

def factor(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)
factor(120)
