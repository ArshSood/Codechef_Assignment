t=int(input())
def prime(p):
    a=set()
    for i in range(2,p+1):
        count=0
        j=2
        while j<=i**0.5:
            if i%j==0:
                count+=1
            j+=1
        if count==0:
            a.add(i)
            #print(a)
    return a
    



for i in range (0,t):
    n=int(input())
    set1=prime(n)
    arr=list(set1)
    #print(arr)
    count=0
    for i in range(0,len(arr)):

        for j in range(0,i+1):
            if arr[i]+arr[j]==n:
                print(arr[i],end=" ")
                print(arr[j],end=" ")
                count+=1
            """if arr[i]+arr[j]>n:
                count+=1"""
        if count==1:
            break
    if count==0:        
        print("-1","-1")
