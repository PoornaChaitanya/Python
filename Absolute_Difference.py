x,y=list(map(int,input().split()))
print(abs(int(str(x)[:y])-int(str(x)[-y:])))