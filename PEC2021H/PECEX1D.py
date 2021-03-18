def stairs(n,x):
    global num
    if x==1:
        count=0
        for i in range(-3,4):
            #count=0
            if n-i==0:
                count+=1
        return count

    count=0
    for i in range(-3,4):
        if 0<=n-i<=num and x!=0:
            count+=stairs(n-i,x-1)
    return count

t=int(input())
for i in range(0,t):
    global num
    num,x=list(map(int,input().split()))
    if num==0 and x==0:
        print(1)
    else:
        Ans=stairs(num,x)
        print(Ans)
    
    