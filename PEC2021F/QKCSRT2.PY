# you can use this less than comparator operator in the choose_pivot, if you would like
# keep in mind that this is the comparator used in the quick sort implementation given
def lessthan(x, y):
    return x[0] < y[0]
 
# complete this function
# the return value is wrong, you are to complete this function so that the return value is correct
# arr is a list of tuples where each tuple contains the pair (x, y)
def choose_pivot(arr):
    dict={""}
    result=[]
    for i in range(0,len(arr)):
        if arr[i][0] not in dict:
            result.append(i)
            dict.add(arr[i][0])
            
            #if arr[i][1]>dict[arr[i][0]]:
                #result.append(i)
                #dict[arr[i][0]]=arr[i][1]
            #dict[arr[i][0]]=arr[i][1]
        else:
            continue

            
    return result


 
# ---------------------------- Do not modify code below this line ------------------------------------
n = int(input())
arr_strip = list(map(int, input().split()))
arr = []
for i in range(0, 2*n, 2):
    arr.append((arr_strip[i], arr_strip[i+1]))
 
candidates = choose_pivot(arr)
 
print(len(candidates))
print(*candidates)