def palin(n):
    return str(n)==str(n)[::-1]
n=int(input())
a=n-1
b=n+1
while True:
    if palin(a) and palin(b):
        print(b,a)
        break
    elif palin(a):
        print(a)
        break
    elif palin(b):
        print(b)
        break
    a-=1
    b+=1
