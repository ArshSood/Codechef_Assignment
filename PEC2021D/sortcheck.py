test=int(input())
for i in range (0,test):
    size=int(input())
    A=list(map(int,input().split()[:size]))
    B=list(map(int,input().split()[:size]))
    count=0
    A.sort()
    #if A.sort()==B:
    for i in range (0,size):
        if A[i]!=B[i]:
            count=1
            
    if count==0:
        print ("yes")
    else:
        print("no")


