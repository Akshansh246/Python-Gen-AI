def last_digit(a, b):
    if b == 0:
        return 1
    cycle = [a % 10]
    for _ in range(3):
        cycle.append((cycle[-1] * (a % 10)) % 10)
    return cycle[(b - 1) % 4]

t = int(input())
answers = []

for _ in range(t):
    a, b = map(int, input().split())
    answers.append(last_digit(a, b))

for x in answers:
    print(x)
