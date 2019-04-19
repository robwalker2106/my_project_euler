"""
This script is to find the 10,001st prime number.  It is problem 7 on www.ProjectEular.net.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the
6th prime is 13.  What is the 10 001st prime number?
"""

from math import floor, sqrt

LIMIT = 10000
COUNT = 1
CANDIDATE = 1

def is_prime(num):
    """
    This function receives an int as an argument and returns True
    if it is a prime number.
    """
    if num == 1:
        return False
    elif num < 4:
        return False
    elif num % 2 == 0:
        return False
    elif num < 9:
        return True
    elif num % 3 == 0:
        return False

    round_squared = floor(sqrt(num))
    factor = 5
    while factor <= round_squared:
        if num % factor == 0:
            return False
        elif num % (factor+2) == 0:
            return False
        factor = factor + 6
    return True

while COUNT < LIMIT:
    CANDIDATE = CANDIDATE + 2
    if is_prime(CANDIDATE):
        COUNT = COUNT + 1

print(CANDIDATE)
