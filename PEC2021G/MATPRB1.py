t=int(input())
for i in range(0,t):
    arr=[]
    n=int(input())
    for j in range(0,n):
        arr.append([])
        arr1=list(map(int,input().split()))
        arr[j]=arr1
        #print(arr)
    def transpose(arr):#very important need to know how 2d list works
        arr1=[]
        for i in range(0,len(arr)):
            arr1.append([])
        #print (arr1)
        for j in range(0,len(arr)):
        
            for i in range(0,len(arr)):
                arr1[j].append(arr[i][j])
            #print (arr1)
        if arr1==arr:
            return 1
        else:
            return 0
    def tri(arr):
        countup=0
        countdown=0
        check=0
        for i in range(0,len(arr)):
            for j in range(0,len(arr)):
                if i>j:
                    if arr[i][j]!=0:
                        countup+=1
                if i<j:
                    if arr[i][j]!=0:
                        countdown+=1
                if i==j:
                    if arr[i][j]!=0:
                        check+=1
        if (countup==0 or countdown==0) and check>0:
            return 1
        else:
            return 0
    def dia(arr):
        countup=0
        countdown=0
        check=0
        for i in range(0,len(arr)):
            for j in range(0,len(arr)):
                if i>j:
                    if arr[i][j]!=0:
                        countup+=1
                if i<j:
                    if arr[i][j]!=0:
                        countdown+=1
                if i==j:
                    if arr[i][j]!=0:
                        check+=1
        if countup==0 and countdown==0 and check>0:
            return 1
        else:
            return 0

    s=transpose(arr)
    t=tri(arr)
    d=dia(arr)
    result=s+2*t+4*d
    print(result)

        

            

