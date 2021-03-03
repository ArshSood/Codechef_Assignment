n = int(input())
print("2")
sum=int(input())
sum1=0
for i in range(0, n-1):
    x = int(input())
    sum1=sum1 +sum*x
    sum=sum+x
print(sum1)