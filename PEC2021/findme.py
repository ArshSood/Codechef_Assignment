N,K=input().split()
K=int(K)
N=int(N)
value=list(map(int,input().split()[:N]))
if K in value:
    print(1)
else:
    print(-1)