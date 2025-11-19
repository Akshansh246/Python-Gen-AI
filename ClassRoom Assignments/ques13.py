N = int(input())
i = 1
turn = "" 
while N > 0:
    N -= i
    if N <= 0:
        turn = "Ramesh"
        break
    N -= 2 * i
    if N <= 0:
        turn = "Suresh"
        break
    i += 1

print(turn)
