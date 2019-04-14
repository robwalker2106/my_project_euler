#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.


primes = [2]

for i in range(3,2000001):
    x = 2
    while i > x:
        if i % x == 0:
            x = 2
            break
        else:
            x = x + 1
    if i == x:
        primes.append(i)
        print(primes[-1])
    else:
        x = 2

print(sum(primes))