#Adam number is a number when reversed, the square of the number and the square
#of the reversed number should be numbers which are reverse of each other.

n=int(input())
m=int(str(n)[::-1])
a=n*n
b=m*m
print(a==int(str(b)[::-1]))