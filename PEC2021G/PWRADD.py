import sys
 
def add(a, b):
    print('1', a, b) 
    sys.stdout.flush()
    return int(input())
# --------------------- Do not touch anything above this line ----------------------
 
# The return value of this function is wrong, write the correct version of this function using the add(a, b) ...
# function defined above.
 
# Note that this function should return (a ** b) % m, you are guaranteed that add(a, b) returns (a + b) % m

def pwr(a, b):
    
    #M=add(a,0)
    #counter=M
    y=1
    for i in range(0,b):
        counter=0
        for j in range(0,a):
            counter=add(counter,y)
        y=counter
       
        #counter*=M
        #counter=add(M*counter,0)
        
    return y
 

# --------------------- Do not touch anything below this line ----------------------
 
a, b = map(int, input().split())
ans = pwr(a, b)
print('2', ans)
 
 