l = []
with open("input", "r") as f:
    for line in f.readlines():
        l.append(line.strip("\n"))

 
def get_neighbours(i, x, y):
    neighbours = set()
    for j in range(x, y):
        for xx in [-1, 0, 1]:
            for yy in [-1, 0, 1]:
                if (xx, yy) == (0, 0):
                    continue
                X, Y = i + xx, j + yy
                if 0 <= X < len(l) and 0 <= Y < len(l[0]):
                    neighbours.add((X, Y))
    return neighbours
 
 
total = 0
for i in range(len(l)):
    j = 0
    while j < len(l[0]):
        if not l[i][j].isdigit():
            j += 1
            continue
        num_end = j + 1
        while num_end < len(l[0]) and l[i][num_end].isdigit():
            num_end += 1
        for x, y in get_neighbours(i, j, num_end):
            if l[x][y] in "0123456789.":
                continue
            num = int(l[i][j:num_end])
            total += num

        j = num_end
 
print(total)
