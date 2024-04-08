#Hwteromecic Number
#Pronic number is a number which is the product of two consecutive integers.

""""
n=int(input())
x=1
while True:
    m=x*(x+1)
    if m==n:
        print(True)
        break
    if m>n:
        print(False)
        break
    x+=1

"""
n=int(input())
if int(n**0.5)*(int(n**0.5)+1)==n:
    print(True)
else:
    print(False)