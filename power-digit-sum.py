#2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2**1000?

num = 2**1000
num_string = str(num)
ans = 0

for i in num_string:
    ans = ans + int(i)

print(ans)