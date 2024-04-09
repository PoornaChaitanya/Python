#a happy number is a number which eventually reaches 1 OR 7 when
# replaced by the sum of the square of each digit.

def summ(n):
    tot=0
    while n:
        tot+=((n%10)**2)
        n//=10
    return tot
n=int(input())
while True:
    if n<10:
        print(n==1 or n==7)
        break
    n=summ(n)