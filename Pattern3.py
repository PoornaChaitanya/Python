"""

EEEEE
DDDD
CCC
BB
A

"""

n=int(input())
for i in range(n):
    print(chr(64+n-i)*(n-i))