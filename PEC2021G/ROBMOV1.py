t=int(input())
for i in range(0,t):
    arr=list(map(int,input().split()))
    Xs,Ys,Xen,Yen=arr
    count=Xen-Xs
    count1=Yen-Ys
    final=abs(count)+abs(count1)
    print(final)
    if count>0:
        print("E"*count,end="")
    else:
        print("W"*abs(count),end="")
    if count1>0:
        print("N"*count1,end="")
    else:
        print("S"*abs(count1),end="")
    print()