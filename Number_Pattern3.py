"""

12345
2345
345
45
5

"""

n=int(input())
for i in range(1,n+1):
    for j in range(i,n+1):
        print(j,end="")
    print()