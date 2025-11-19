l = int(input())
i = 1
j = 1
for i in range(l):
    for j in range(i+1):
        print('#',end="")
        j=j+1
    print()
    i=i+1

