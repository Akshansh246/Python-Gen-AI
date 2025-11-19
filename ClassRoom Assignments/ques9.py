t = int(input())
answers = []

for _ in range(t):
    N = int(input())
    A = (N // 2) + 1
    answers.append(A)

for x in answers:
    print(x)
