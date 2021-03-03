N=int(input())
if N==1:
    print("0")
    exit()

i=2
while(i<=N**(1/2)):
    
    if(N%i==0):

       print("0")
       exit()
    i=i+1
print("1")