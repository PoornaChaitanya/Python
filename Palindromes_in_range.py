def palin(n):
    if n==n[::-1]:
        return True
    return False
x,y=list(map(int,input().split()))
l=[]
cnt=0
for i in range(x,y+1):
    if palin(str(i)):
        cnt+=1
        l.append(i)
print("Count =",cnt)
print("Palindromes =",*l)