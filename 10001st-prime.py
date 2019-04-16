#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

from math import floor,sqrt

limit = 10001
count = 1
candidate = 1

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
    
while count < limit:
    if is_prime(candidate):
        count = count + 1
    candidate = candidate + 1

print(candidate)

#primes = [2]
#i = 3

#def current(num):

 #   for p in primes:
  #      if num % p == 0:
   #         return False
    #return True
        
#while len(primes) < 10001:
 #   c = primes[-1]
  #  stop = current(i)
   # if stop and i > c:
    #    while i > c:
     #       if i % c == 0:
      #          break
       #     else:
        #        c = c + 1
    #if i == c:
     #   primes.append(i)
    #i = i + 1

    #print(primes[-1])

# print(primes[-1])