n=int(input())
i=1
while True:
    s=i*i
    if s>n:
        print(False)
        break
    if s==n:
        print(True)
        break
    i+=1