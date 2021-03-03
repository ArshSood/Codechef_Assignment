n=int(input())
i=1
while i<=n:
    count=i
    while count<=2*i-1:
        print(count,end=" ")
        count+=1
    count-=2
    while count>=i:
        print(count,end=" ")
        count-=1
    i+=1
    print()



