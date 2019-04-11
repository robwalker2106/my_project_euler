
#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99
#Find the largest palindrome made from the product of two 3-digit numbers.

a = 999
b = 999
ans = []

def check(num):
    """
    This functions receives an interger as an argument and returns True
    if the interger is a palindrome and False if it is not.
    """
    num_string = str(num)
    f = 0
    l = -1


    for _ in range(len(num_string)/2):
        if num_string[f] == num_string[l]:
            f = f + 1
            l = l - 1
        else:
            return False
    
    return True

while b > 99:
    while not check(a * b):
        if a > 101:
            a = a - 1
        else:
            a = 999
            b = b - 1
            continue
    ans.append(a * b)
    b = b - 1

print(max(ans))


    


