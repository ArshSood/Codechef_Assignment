n=int(input())
i=1
count=1
while i<=n:
    if i%2!=0:
        count=(i-1)*5+1
        while count<=i*5:
            print(count,end=" ")
            count+=1
        i+=1
        print()
    else:
        count=i*5
        while count>(i-1)*5:
            print(count,end=" ")
            count-=1
        i+=1
        print()

