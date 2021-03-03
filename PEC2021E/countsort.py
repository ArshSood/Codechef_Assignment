test=int(input())
for i in range (0,test):
    n=int(input())
    li=list(map(int,input().split()[:n]))
    li.sort()

    
    for j in range (0,n):
        print(li[j],end=" ")
    print()