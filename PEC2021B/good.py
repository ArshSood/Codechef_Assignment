n=int(input())
count=0
i=2
while i<=n**0.5:
    if n%i==0:
        count+=i
        count+=(n//i)
        if count+1>n:
            print("NO")
            exit()
    i+=1
if count+1==n: 
    print("YES")
else:
    print("NO")
