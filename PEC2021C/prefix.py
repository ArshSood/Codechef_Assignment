n = int(input())
arr = []
ans = 1
max=int(input())
for i in range(0, n-1):
    x = int(input())
    if x>max:
        ans+=1
        max=x


print(2)
print(ans)