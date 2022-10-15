n=int(input())
ec=0
oc=0
for i in str(n):
    if int(i)%2==0:
        ec+=1
    else:
        oc+=1
if ec>0 and oc==0:
    print("Even")
elif ec==0 and oc>0:
    print("Odd")
else:
    print("Mixed")