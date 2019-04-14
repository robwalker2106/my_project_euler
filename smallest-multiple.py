#2520 is the smallest number that can be 
#divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is
#evenly divisible by all of the numbers from 1 to 20?

nums = [n for n in range(2,21)]
prime_nums = [2]
x = 2

for i in nums:
    while x < i:
        if i % x == 0:
            break
        else:
            x = x + 1
            if x == i:
                prime_nums.append(i)
                x = 2
                break

print(prime_nums)