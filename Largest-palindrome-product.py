
#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99
#Find the largest palindrome made from the product of two 3-digit numbers.

ans = []

for x in range(100,1000):
    for y in range(100,1000):
        f = str(x * y)
        b = f[::-1]
        if f == b:
            ans.append(x * y)

print(max(ans))
