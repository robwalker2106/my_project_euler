#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?


primes = [2]
i = 3

def current(num):

    for p in primes:
        if num % p == 0:
            return False
    return True
        
while len(primes) < 10001:
    c = primes[-1]
    stop = current(i)
    if stop and i > c:
        while i > c:
            if i % c == 0:
                break
            else:
                c = c + 1
    if i == c:
        primes.append(i)
    i = i + 1

    print(primes[-1])

print(primes[-1])