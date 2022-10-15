n=int(input())
ans=0

if n<0:
    print(False)
else:
    for i in range(1,n//2+1):
        if n%i==0:
            ans+=i
    if ans==n:
        print(True)
    else:
        print(False)
    