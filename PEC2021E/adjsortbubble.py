n=int(input())
li=list(map(int,input().split()[:n]))
def bubble(given): 
    arr=[]
    count=0
    for i in range(0,len(li)):
        swapped=False
        for j in range (0,len(li)-i-1):
            if li[j]>li[j+1]:
                li[j+1],li[j]=li[j],li[j+1]
                swapped=True
                arr.append(j)
                count+=1
        if not swapped:
            print(count)
            for x in arr:
                print(x,end=" ")
            return
bubble(li)


