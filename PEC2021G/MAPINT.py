n=int(input())
arr=[]
dict={}
dict1={}
counter=set()
count=0

for i in range(0,n):
    tup=tuple(input().split())
    arr.append(tup)
for i in range(0,n):
    if arr[i][0] not in counter:
        dict[arr[i][0]]={arr[i][2]}
        dict1[arr[i][0]]=[arr[i][3]]
        counter.add(arr[i][0])
    else:
        dict[arr[i][0]].add(arr[i][2])
        dict1[arr[i][0]].append(arr[i][3])
       
    if arr[i][1] not in counter:
        dict[arr[i][1]]={arr[i][2]}
        dict1[arr[i][1]]=[arr[i][3]]
        counter.add(arr[i][1])
    else:
        dict[arr[i][1]].add(arr[i][2])
        dict1[arr[i][1]].append(arr[i][3])
#print(dict1['4'])    
for i in dict:
    if len(dict[i])==2 and len(dict1[i])==4:
        count+=1
    #print(i,dict[i])
print(count)
#print(counter)

























"""for i in range(0,n):
    if arr[i][0] not in counter:
        temp=arr[i][0]
        counter.add(temp)
        if arr[i][3] in refer:
            street=set(arr[i][2])
        else:
            street1=set(arr[i][2])

        for j in range(0,n):
            if i!=j:
                if temp==arr[j][0] or temp==arr[j][1]:
                    if arr[j][3] in refer:
                        street.add(arr[j][2])
                    else:
                        street1.add(arr[j][2])
        if len(street)==1 and len(street1)==1:
            count+=1"""



