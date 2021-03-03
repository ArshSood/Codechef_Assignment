import math
n=int(input())
dict={}
cal=0
for i in range(0,n):
    s=input()
    plate=input()
    time=int(input())
    if s=="entry":
        dict[plate]=time
    else:
        time=time-dict[plate]
        time=time/60
        time=math.ceil(time)
        if time>1:
            cal+=(time-1)*30+60
        else:
            cal+=60

print(cal)




