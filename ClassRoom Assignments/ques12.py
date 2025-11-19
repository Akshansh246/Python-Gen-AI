import math

t = int(input())
answers = []

for _ in range(t):
    x, y = map(int, input().split())
    gcd_val = math.gcd(x, y)
    lcm_val = (x * y) // gcd_val
    answers.append((gcd_val, lcm_val))

for g, l in answers:
    print(g, l)
