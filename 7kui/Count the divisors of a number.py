"""
Count the number of divisors of a positive integer n.

Random tests go up to n = 500000.

Examples (input --> output)

4 --> 3 (1, 2, 4)
5 --> 2 (1, 5)
12 --> 6 (1, 2, 3, 4, 6, 12)
30 --> 8 (1, 2, 3, 5, 6, 10, 15, 30)
"""

"""
#var1
def divisors(n):
    divisors = 0

    for i in range(1, n + 1):
        if n % i == 0: divisors += 1

    return divisors
"""

def divisors(n):
    return len([i for i in range(1, n + 1) if n % i == 0])
