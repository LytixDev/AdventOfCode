with open("input_proper") as f:
    d = [l.strip() for l in f.readlines()]

instructions = d[0]
d = d[2:]
# should use a binary tree but cant find any in the stdlib

tree = {}
for l in d:
    parent, children = l.split(" = ")
    children = children[1:-1].split(", ")
    tree[parent] = children

i = 0
s = "AAA"
goal = "ZZZ"
while True:
    for instruction in instructions:
        i += 1
        idx = 0 if instruction == "L" else 1
        s = tree[s][idx]
        if s == goal:
            print(i)
            exit(0)
