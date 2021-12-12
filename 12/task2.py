with open("input.txt", "r") as f:
    data = [line.strip("\n").split("-") for line in f.readlines()]

dct = {}
for i in data:
    if i[0] not in dct:
        dct.setdefault(i[0], [])
    for v in i[1:]:
        dct[i[0]].append(v)
        # i -> ["a", "b"]. Need to add a to b and b to a. Above loop adds a to b. Below adds b to a.
        if i[0] != "start":
            if v not in dct:
                dct[v] = [i[0]]
            else:
                dct[v].append(i[0])


def dfs(key, p):
    if key != "end" and key != "start":
        if key.lower() in p.split(","):
            count = 0
            for v in p.split(","):
                if p.count(v) > 1 and v.lower() == v:
                    count += 1
            if count > 1:
                return 0
            else:
                for val in dct[key]:
                    dfs(val, p + "," + key)
        else:
            for val in dct[key]:
                dfs(val, p + "," + key)

    elif key == "end":
        paths.append(p + "," + key)
            

paths = []
for v in dct["start"]:
    dfs(v, "start")

print(len(paths))
