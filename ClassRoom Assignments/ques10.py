N = int(input())
X = int(input())

ans = []

for _ in range(N):
    Y = int(input())
    if Y >= X:
        ans.append("YES")
    else:
        ans.append("NO")

for i in ans:
    print(i)
