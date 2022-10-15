def sel(n):
    s=n
    while n>0:
        k=n%10
        n=n//10
        if k==0 or s%k!=0:
            return False
    return True
n=int(input())
m=int(input())
for i in range(n,m+1):
    if sel(i):
        print(i,end=" ")