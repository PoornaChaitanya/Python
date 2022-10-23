n=int(input())
m=n
for i in range(n):
    for j in range(1,m+1):
        print(j,end="")
    m-=1
    print()