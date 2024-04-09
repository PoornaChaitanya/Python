#Ugly numbers are numbers whose only prime factors are 2, 3 or 5

n=int(input())
for i in [2,3,5]:
    while n%i==0:
        n=n//i
print(n==1)