N=int(input())
i=1
counter=10
while i<=N:
    if i%2==0:
        print(i,end="")
        i+=1
    else:
        print(counter,end="")
        counter+=10
        i+=1
    

