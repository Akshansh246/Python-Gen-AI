N = int(input())
answers = []

for _ in range(N):
    SH, SM, EH, EM = map(int, input().split())
    start = SH * 60 + SM
    end =  EH * 60 + EM
    diff = end - start
    hours = diff // 60
    minutes  = diff % 60
    answers.append((hours, minutes))

for h, m in answers:
    print(h, m)
