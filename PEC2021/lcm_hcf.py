N,M=input().split()
N=int(N)
M=int(M)
n,m=N,M
if M>N:
    N,M=M,N
while N%M !=0:
    i=N
    N=M
    M=i%M
hcf=M
lcm=int((n*m)/hcf)
print(hcf,lcm)


