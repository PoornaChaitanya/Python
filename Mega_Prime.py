#A 'megaprime' number is a prime number and its individual
# digits are also prime.

def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
if prime(n):
    while n:
        if prime(n%10)==False:
            print("False")
            break
        n//=10
    else:
        print("True")
else:
    print("False")