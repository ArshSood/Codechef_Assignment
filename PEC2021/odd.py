L,R=input().split()
L=int(L)
R=int(R)
if L%2==0:
    L=L+1
while L<=R:
    print(L,end=" ")
    L=L+2

