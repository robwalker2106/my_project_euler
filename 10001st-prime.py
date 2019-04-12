



prime_nums = [2]
x = 2
i = 2

while len(prime_nums) < 10006:
    while x < i:
        if i % x == 0:
            break
        else:
            x = x + 1
            if x == i:
                prime_nums.append(i)
                x = 2
                break
    i = i + 1


print(prime_nums[5])
