with open("input") as f:
    l = [line.strip("\n") for line in f.readlines()]

config = { "red": 12, "green": 13, "blue": 14 }
accum = 0
for id, game in enumerate(l):
    _, g = game.split(":")
    possible = True
    for s in g.split(";"):
        for c in s.split(","):
            n, cidx = c[1:].split(" ")
            if int(n) > config[cidx]:
                possible = False
    if possible:
        accum += id + 1

print(accum)
