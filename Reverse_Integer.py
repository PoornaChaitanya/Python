n=int(input())
if n>0:
    print(int(str(n)[::-1]))
else:
    n*=-1
    print(-1*int(str(n)[::-1]))