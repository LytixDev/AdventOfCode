from collections import defaultdict

X = [line.strip("\n") for line in open("input.txt").readlines()]

path = []
sizes = defaultdict(int)
for cmd in X:
    if "$ ls" in cmd or "dir" in cmd:
        continue

    if "$ cd" in cmd:
        arg = cmd.split(" ")[2]
        path.pop() if arg == ".." else path.append(arg)
    else:
        file_size = cmd.split(" ")[0]
        #sizes["".join(p for p in path)] += int(file_size)
        for i in range(1, len(path) + 1):
            sizes["/".join(path[:i])] += int(file_size)

# p1
print(sum(list(filter(lambda x: x <= 100000, sizes.values()))))

# p2
free = sizes['/'] - (70000000 - 30000000)
print(min(list(filter(lambda x: x > free, sizes.values()))))

#candidates = []
#for val in sizes.values():
#    if val > free:
#        candidates.append(val)
#
#print(min(candidates))
