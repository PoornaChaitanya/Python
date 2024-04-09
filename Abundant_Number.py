#abundant number or excessive number is a positive integer for
# which the sum of its proper divisors is greater than the number.

n=int(input())
ans=0
for i in range(1,n//2+1):
    if n%i==0:
        ans+=i
if ans>n:
    print("True")
else:
    print("False")
    