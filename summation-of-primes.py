#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.


primes = [2]
c = 2



def current(num):

    for p in primes:
        if num % p == 0:
            return False
    return True
        

for i in range(3,2000001): 
    while i > c:
        if current(i):
            c = primes[-1] + 1
        if i == c:
            primes.append(i)
            print(primes[-1])
            break
        c = primes[-1] + 1

        

        
    


print(sum(primes))