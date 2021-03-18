t=int(input())
for i in range(0,t):
    li=list(map(int,input().split()))
    li.sort()
    print(li[2])