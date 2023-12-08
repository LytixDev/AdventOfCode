import math

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

i = 1
keys = set([key for key in tree.keys() if key[-1] == "A"])
steps = []

def get_steps(start):
    this = start
    i = 0
    while True:
        for instruction in instructions:
            i += 1
            idx = 0 if instruction == "L" else 1
            this = tree[this][idx]
            if this[-1] == "Z":
                return i


step_count = [get_steps(key) for key in keys]
print(math.lcm(*step_count))
