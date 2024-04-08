#Add the given digit until a single digit is obtained
n=int(input())
if n==0:
    print(0)
elif n%9==0:
    print(9)
else:
    print(n%9)