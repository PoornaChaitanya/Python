def sdn(n):
    if n==0:
        return False
    x=n
    while x:
        s=x%10
        x=x//10
        if s==0 or n%s!=0:
            return False
    return True
x,y=list(map(int,input().split()))
l=[]
cnt=0
for i in range(x,y+1):
    if sdn(i):
        cnt+=1
        l.append(i)
print("Count =",cnt)
print("Numbers =",*l)