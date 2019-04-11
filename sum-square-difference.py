#The sum of the squares of the first ten natural numbers is,
#      1**2 + 2**2 + ... + 10**2 = 385
#The square of the sum of the first ten natural numbers is,
#      (1 + 2 + ... + 10)**2
#Hence the difference between the sum of the squares of the first ten natural numbers
#and the square of the sum is 3025 - 385 = 2640.

#Find the difference between the sum of the squares of the first
#one hundred natural numbers and the square of the sum.

a = 0
b = 0

for i in range(1,101):
    b = b + i**2

for i in range(1,101):
    a = a + i

print((a**2)-b)

