"""
This script is to find the largest prime factor from the number
600851475143.  This is promblem 3 on www.ProjectEular.net.
"""

X = 2
I = 600851475143

while X < I:
    if I % X == 0:
        I = I / X
    else:
        X = X + 1

print(X)
