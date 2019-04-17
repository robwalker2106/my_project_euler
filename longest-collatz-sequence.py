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

values = {1: 1}

def collatz_seq(n):
    if n in values:
        return values[n]
    if n % 2 ==0:
        values[n] = 1 + collatz_seq(n/2)
    else:
        values[n] = 2 + collatz_seq(((3 * n) + 1)/2)
    return values[n]


for i in range(500001,1000001):
    if collatz_seq(i) > ans:
        ans = collatz_seq(i)
        num = i

print(num)    
