with open("input_proper") as f:
    lines = [l.strip() for l in f.readlines()]

seeds = list(int(s) for s in lines.pop(0).split(": ")[1].split())

maps = []
this = []
for l in lines[1:]:
    if l.endswith("map:"):
        this = []
        continue
    if l == "":
        maps.append(this)
        continue
    dest, source, range_len = (int(n) for n in l.split())
    this.append((source, dest, range_len))
maps.append(this)


def get_loc(loc, mapings):
    for dest, source, range_len in mapings:
        offset = dest - source
        if loc >= source and loc < source + range_len:
            return loc + offset
    return loc


seeds = list(zip(seeds[::2], seeds[1::2]))


def loc_in_seeds(loc):
    for seed, range_len in seeds:
        if loc >= seed and loc <= seed + range_len:
            return True
    return False


i = 0
while True:
    if i % 10_000 == 0:
        print(i)
    loc = i
    for m in maps[::-1]:
        #print(loc, m)
        loc = get_loc(loc, m)

    #print(loc)
    if loc_in_seeds(loc):
        print(i)
        break
    i += 1
