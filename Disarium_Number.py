#A number is said to be the Disarium number when the sum of its digit raised
#to the power of their respective positions is equal to the number itself.

n=int(input())
x=len(str(n))
summ=0
m=n
while x:
    summ+=(m%10)**x
    m//=10
    x-=1
print(summ==n)
