N=int(input())

value=list(map(int,input().split()[:N]))
N-=1
while N>=0:
    print (value[N],end=" ")
    N=N-1