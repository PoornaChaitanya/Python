def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
x,y=list(map(int,input().split()))
cnt=0
l=[]
for i in range(x,y+1):
    if prime(i):
        cnt+=1
        l.append(i)
print("Count =",cnt)
print("Primes =",*l)
