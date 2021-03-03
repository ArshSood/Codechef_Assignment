n = int(input())
set={""}
for i in range(0, n):
    x = int(input())
    set.add(x)
set.remove("")
q = int(input())
print("1")
for i in range(0, q):
    x = int(input())
    if x in set:
        print('yes')
    else:
        print('no')