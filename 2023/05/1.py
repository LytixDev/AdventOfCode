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
    this.append(tuple(int(n) for n in l.split()))
maps.append(this)


def get_loc(loc, mapings):
    for dest, source, range_len in mapings:
        offset = dest - source
        if loc >= source and loc < source + range_len:
            return loc + offset
    return loc


locs = []
for seed in seeds:
    loc = seed
    for m in maps:
        loc = get_loc(loc, m)
    locs.append(loc)

print(min(locs))
