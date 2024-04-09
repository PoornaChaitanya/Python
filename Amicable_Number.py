#A number is called an Automorphic number if and only if its square ends
# in the same digits as the number itself. 

def div(n):
    summ=1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            summ+=i+(n/i)
    return summ
x,y=list(map(int,input().split()))
print(div(x)==y and div(y)==x)