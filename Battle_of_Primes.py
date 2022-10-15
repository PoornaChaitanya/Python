def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
m=int(input())
s=n+m
cn=0
while True:
    cn+=1
    s+=1
    if prime(s):
        print(cn)
        break