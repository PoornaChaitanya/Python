p,r,t=list(map(int,input().split()))
ci=p*(1+r/100)**t
print("{:.2f}".format(ci))