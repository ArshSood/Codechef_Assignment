test=int(input())
for i in range(0,test):
    dict={}
    keys=[]
    n=int(input())
    m=int(input())
    for i in range (0,n):
        l,r=input().split()
        l=int(l)
        r=int(r)
        if dict.get(l)==None:
            dict.update({l:1})
            keys.append(l)
        else:
            dict[l]+=1
        if dict.get(r+1)==None:
            dict.update({r+1:-1})
            keys.append(r+1)
        else:
            dict[r+1]-=1

    max1=0
    sum=0
    keys.sort()
    for i in keys:
        sum+=dict[i]
        max1=max(sum,max1)
      
    print(max1)

    
