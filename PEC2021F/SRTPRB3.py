# Correct this function so that the correct output is given
def get_distinct_fractions(arr):
    dict={}
    count=-10**9
    countpos=10**9
    for i in range(0,len(arr)):
     
        if arr[i][0]<0 and arr[i][1]==0:
            if arr[i][0]>count:
                count=arr[i][0]
        elif arr[i][0]>0 and arr[i][1]==0:
            if arr[i][0]<countpos:
                countpos=arr[i][0]
        elif arr[i][1]!=0:
            arr1=[]

            if arr[i][0]/arr[i][1] in dict :
                arr1=dict[arr[i][0]/arr[i][1]]
                if abs(arr[i][0])<abs(arr1[0]):
                    dict[arr[i][0]/arr[i][1]]=[arr[i][0],arr[i][1]]
                elif arr[i][1]>0 and arr1[1]<0:
                    dict[arr[i][0]/arr[i][1]]=[arr[i][0],arr[i][1]]
                   

                """if arr[i][0]/arr[i][1]<0:
                    arr1=dict[arr[i][0]/arr[i][1]]
                    if arr1[1]<0 and arr[i][0]<0:
                       dict[arr[i][0]/arr[i][1]]=[arr[i][0],arr[i][1]]
                    elif arr1[0]<0 and arr[i][0]<0:
                        if arr1[0]<arr[i][0]:
                            dict[arr[i][0]/arr[i][1]]=[arr[i][0],arr[i][1]]
                    elif arr1[1]<0 and arr[i][1]<0:
                        if arr1[0]>arr[i][0]:
                            dict[arr[i][0]/arr[i][1]]=[arr[i][0],arr[i][1]]
                if arr[i][0]/arr[i][1]>0:
                    arr1=dict[arr[i][0]/arr[i][1]]
                    if abs(arr[i][0])<abs(arr1[0]):
               
                        dict[arr[i][0]/arr[i][1]]=[arr[i][0],arr[i][1]]"""
            else:
                dict[arr[i][0]/arr[i][1]]=[arr[i][0],arr[i][1]]
    arr=[]
    keys=list(dict.keys())
    keys.sort()
    for i in keys:
        arr.append(dict[i])
    if countpos!=10**9:
        arr.append([countpos,0])
    if count!=-10**9:
        arr.insert(0,[count,0])
    return arr

        
                



            

        
 
# ----------------------Do not change anything below this line --------------------------
 
n = int(input())
arr_strip = list(map(int, input().split()))
arr = []
for i in range(0, 2*n, 2):
    arr.append((arr_strip[i], arr_strip[i+1]))
 
result = get_distinct_fractions(arr)
print(len(result))
for x in result:
    print(x[0], x[1], end = ' ')