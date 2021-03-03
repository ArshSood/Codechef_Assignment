n=int(input())
li=list(map(int,input().split()[:n]))

def mergesort(list):
    ans=0
    if(len(list)==2):
        if(list[0]!=list[1]):
            return 1
        else:
            return 0
    mid=len(list)//2
    lefthalf=mergesort(list[0:mid])
    righthalf=mergesort(list[mid:len(list)])
    A=set(list[:mid])
    B=set(list[mid:])
    if(A&B):
        return lefthalf+righthalf
    else:
        return lefthalf+righthalf+1

    
print(mergesort(li))
   