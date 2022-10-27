for t in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    for i in range(b):
        l.insert(0,l.pop())
    print(*l)
