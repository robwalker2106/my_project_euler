#Collatz Sequence
#
#if n is even, then n/2
#if n is odd, the 3n + 1
#
# example for 13
# 13 => 40 => 20 => 10 => 5 => 16 => 8 => 4 => 2 => 1
#Which starting number under 1,000,000 produces the longest collatz sequence?

ans = 0
num = 0

def collatz_seq(n):
    count = 1
    while n > 1:
        if n % 2 == 0:
            n = n/2
            count = count + 1
        else:
            n = (3 * n) + 1
            count = count + 1
    return count


for i in range(1000001):
    x = collatz_seq(i)
    if x > ans:
        ans = x
        num = i

print(num)    