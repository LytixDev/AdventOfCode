import re

# majorly retarded, but werks
data = [line.strip("\n") for line in open("input.txt", "r")]
stacks_count = 9
split_idx = 0
stacks = [[] for _ in range(stacks_count)]
PART_ONE = False

for i, d in enumerate(data):
    if "[" not in d:
        split_idx = i + 2
        break

    for j in range(stacks_count):
        offset = 0 if j == 0 else 2
        char = d[1+4*j]
        if char != " ":
            stacks[j].append(char)

for d in data[split_idx:]:
    n, f, t = re.findall('\d+', d)
    if PART_ONE:
        for _ in range(int(n)):
            item = stacks[int(f) - 1].pop(0)
            stacks[int(t) - 1].insert(0, item)
    else:
        items = stacks[int(f) - 1][:int(n)]
        stacks[int(f) - 1] = stacks[int(f) - 1][int(n):]
        [stacks[int(t) - 1].insert(0, item) for item in items[::-1]]

print("".join(stack[0] for stack in stacks))

