n=input()
n=n.split()
x=0
y=0
for i in n:
    x+=ord(max(i))
    y+=ord(min(i))
print(x-y)