n=int(input())
arr=[]
i=1
while i<=n:
    arr.append(int(input()))
    i+=1

while len(arr)>1:
    arr.sort()
    mini=arr[0]
    mins=arr[1]
    counter=2
    while mins==mini and counter<n:
        mins=arr[counter]
        counter+=1
    value=(3*mini+2*mins)%100
    arr.remove(mini)
    arr.remove(mins)
    arr.insert(0,value)
print(arr[0])