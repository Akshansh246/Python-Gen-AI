def reverse_num(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10   
        n //= 10                 
    return rev

t = int(input()) 
ans = []

for _ in range(t):
    a, b = map(int, input().split())
    ra = reverse_num(a)
    rb = reverse_num(b)
    s = ra + rb
    ans.append(reverse_num(s))

for i in ans:
    print(i)