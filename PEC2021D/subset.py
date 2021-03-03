test=int(input())
for k in range(0,test):

    n=int(input())
    li=[]
    for i in range(1,n+1):
        li.append(i)
#li.reverse()
    for i in range(1,(2**n)):
        binary=[]
        while i!=0:
            if i%2==0:
                binary.append(0)
            else:
                binary.append(1)
            i=i//2
        for j in range(0,len(binary)):
            if binary[j]==1:
                print (li[j],end=" ")
        print()


