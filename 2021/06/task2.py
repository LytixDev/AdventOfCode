fish = []
with open("input.txt", "r") as f:
    fish = [int(item) if "\n" not in item else int(item[0:-1]) for item in f.readlines()[0].split(",")]


map = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

for i in fish:
    map[i] += 1

n = 256 -1
for _ in range(n):
    #print(_, sum(map.values()) - map[9])
    tmp = {}
    for key, value in map.items():
        if key != 0:
            tmp[key-1] = value

    tmp[9] = tmp[0]
    tmp[7] += tmp[0]
    map = tmp

sum = 0
for key, val in map.items():
    if key != 9:
        sum += val
print(sum)
