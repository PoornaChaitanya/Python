#A positive integer is called a spy number if the sum and product of
# its digits are equal.

n=int(input())
x=n
summ=0
product=1
while x:
    s=x%10
    x//=10
    summ+=s
    product*=s
print(summ==product)