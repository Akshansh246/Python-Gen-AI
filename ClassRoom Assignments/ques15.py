n = int(input())
result = []
for i in range(n):
    row = [1] 
    if i > 0:
        for j in range(1, i):
            row.append(prev[j - 1] + prev[j])
        row.append(1)
    result.append(row)
    prev = row 

for row in result:
    print(*row)
