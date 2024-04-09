"""

0xxxx
x0xxx
xx0xx
xxx0x
xxxx0

"""

n=5
l=list("x")*n
l[0]='0'
for i in range(n):
    print("".join(l))
    if i<n-1:
        l[i],l[i+1]=l[i+1],l[i]