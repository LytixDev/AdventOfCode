with open("input") as f:
    l = [line.strip("\n") for line in f.readlines()]

accum = 0
for id, game in enumerate(l):
    _, g = game.split(":")
    maxs = { "red": 1, "blue": 1, "green": 1 }
    for s in g.split(";"):
        for c in s.split(","):
            n, cidx = c[1:].split(" ")
            if maxs[cidx] < int(n):
                maxs[cidx] = int(n)

    product = 1
    for v in maxs.values():
        product *= v

    accum += product


print(accum)
