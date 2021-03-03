n=int(input())
array=list(map(int,input().split()))
i=0
count=[]
counter=0
while i<len(array):
    min=i
    start=i+1
    while(start<len(array)):
        if array[start]<array[min]:
            min=start
        start+=1
    if i!=min:
        array[i],array[min]=array[min],array[i]
        count.append(i)
        count.append(min)
        counter+=1
    i+=1
print(counter)
for i in range(0,len(count)):
    print(count[i],end=" ")