def prime(n):
    if n<=1:
        return ("PRIME")
    for i in range(2,int(n**(0.5))+1):
        if n%i==0:
            return ("NOT PRIME")
    return ("PRIME")
print(prime(int(input())))