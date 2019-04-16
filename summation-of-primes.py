#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

from math import sqrt,floor

limit = 2000000
sum = 5
n = 5

def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return False
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    
    r = floor(sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        elif n % (f+2) == 0:
            return False
        f = f + 6
    return True


while n <= limit:
    if is_prime(n):
        sum = sum + n
    n = n + 2
    if n <= limit and is_prime(n):
        sum = sum + n
    n = n + 4

print(sum)


