t=int(input())
for i in range(0,t):
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    counter=A
    Ans=0
    count=0
    for j in range(0,n):
        if B[j] in counter:
            count+=1
            counter.remove(B[j])
            if count>Ans:
                Ans=count
        
        
        elif count>Ans:
            Ans=count
            count=0
            counter=A
        else:
            count=0
            counter=A
    print(Ans)
    

    
    

