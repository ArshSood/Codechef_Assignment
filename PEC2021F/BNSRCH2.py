import sys
 
def find_pos(x):
    print('1 ' + str(x))
    sys.stdout.flush()
    t = int(input())
    return t
# ----------------- Do not modify anything above this line -----------------------
# Complete this function count(n, x), this returns 0 always and hence is wrong, it should return the number of occurrences of x in Chef's array
# You can use the function find_pos(x) to find the value of the element at position x (0 indexed)
# If the index is invalid or you use more than 40 queries to obtain the value, you will receive Wrong Answer
# Chef's array size is not more than 10 ** 5
def count(n, x):
    L,H=1,n-1
    Low=-1
    High=n
    while L<=H:
        mid=L+(H-L)//2
    
        value=find_pos(mid)
        if x<=value:
            H=mid-1
        else:
            L=mid+1
            Low=mid
    
    
    L,H=1,n-1
    while L<=H:
        mid=L+(H-L)//2
        value=find_pos(mid)
        if x<value:
            H=mid-1
            High=mid
        else:
            L=mid+1
    
   
    count=High-Low-1
    return count
    """while True:
                if find_pos(temp)==x:
                    count+=1
                    temp-=1
                else:
                    break
            temp=mid+1
            while True:
                if find_pos(temp)==x:
                    count+=1
                    temp+=1
                else:
                    break
    if find_pos(mid)==x:
    L=mid+1
        else:
            H=mid-1
    if find_pos(H)==x:
        High=H
    else:
        High=L
    L,H=0,n-1
    while L<=H:
        mid=L+(H-L)//2
        if find_pos(mid)==x:
            H=mid-1

        else:
            L=mid+1
    if find_pos(L)==x: Second attempt
        Low=L
    else:
        Low=H
    count=High-Low""" 
                
                
                
                

 
# ----------------- Do not modify anything below this line -----------------------
 
n = int(input())
x = int(input())
 
print('2 ' + str(count(n, x)))
 