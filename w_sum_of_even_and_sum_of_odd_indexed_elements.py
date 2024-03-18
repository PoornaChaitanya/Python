n=int(input())
l=list(map(int,input().split()))
even=0
odd=0
for i in range(n):
    if i%2==0:
        even+=l[i]
    else:
        odd+=l[i]
print(max(even,odd)-min(even,odd))