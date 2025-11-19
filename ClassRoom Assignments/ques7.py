def count_notes(amount, deno):
    denoms = [100, 50, 20, 10, 5, 2, 1]
    if deno in denoms:
        idx = denoms.index(deno)
    else:
        print("Invalid starting denomination!")
        return
    for d in denoms[idx:]:
        num = amount // d
        amount = amount % d
        print(f"{d} rupees note: {num}")
amt = int(input().strip())
start = int(input().strip())
count_notes(amt, start)
