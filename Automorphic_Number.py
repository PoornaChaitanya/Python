#A number is called an Automorphic number if and only if its square ends in the same
# digits as the number itself. 

n=int(input())
m=n*n
print(str(n)==str(m)[len(str(n)):])
