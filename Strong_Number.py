#A strong number is a positive integer whose sum of factorials of its 
#digits equals the number itself.

def fact(n):
    if n==1:
        return 1
    return fact(n-1)*n
n=int(input())
total=0
x=n
while x:
    s=x%10
    x//=10
    total+=fact(s)
print(n==total)

