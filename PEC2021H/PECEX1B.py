import math
t=int(input())
for i in range(0,t):
    num=int(input())
    li=[]
    for j in range(1,math.floor(num**0.5+1)):
        for k in range(j,math.floor(num**0.5+1)):
            if j**2+k**2==num:
                li.append([k,j])
                #print(li)
        #if len(li)==4:
            #break
    li.sort()
    #print(li)
    if len(li)<2:
        print(-1,-1,-1,-1)
    #elif li[1]>li[3]:
        #print(li[2],li[3],li[0],li[1])
    else:
        print(li[0][1],li[0][0],li[1][1],li[1][0])