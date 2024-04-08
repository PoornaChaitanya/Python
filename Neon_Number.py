#A neon number is a number where the sum of digits of
# square of the number is equal to the number.

n=int(input())
m=n*n
summ=0
while m:
    summ+=(m%10)
    m//=10
print(n==summ)
