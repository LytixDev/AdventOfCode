X = [line.strip("\n") for line in open("input.txt").readlines()]
head_x = head_y = tail_x = tail_y = 0

visited = []
visited.append((tail_x, tail_y))

dirs = {
    "R": [0, 1],
    "L": [0, -1],
    "U": [1, 0],
    "D": [-1, 0]

}


def move(x, y):
    global head_x, head_y, tail_x, tail_y

    head_x += x
    head_y += y
    if not (abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1):
        if head_x == tail_x:
            add_x = 0
        else:
            add_x = (head_x - tail_x) / abs(head_x - tail_x)
        if head_y == tail_y:
            add_y = 0
        else:
            add_y = (head_y - tail_y) / abs(head_y - tail_y)

        tail_x += add_x
        tail_y += add_y


def move2(x, y):
    global p

    p[0][0] += x
    p[0][1] += y

    for i in range(1, 10):
        head_x, head_y = p[i - 1]
        tail_x, tail_y = p[i]

        if not (abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1):
            if head_x == tail_x:
                add_x = 0
            else:
                add_x = (head_x - tail_x) / abs(head_x - tail_x)
            if head_y == tail_y:
                add_y = 0
            else:
                add_y = (head_y - tail_y) / abs(head_y - tail_y)

            tail_x += add_x
            tail_y += add_y


for line in X:
    dir, n = line.split(" ")
    x, y = dirs[dir]
    for _ in range(int(n)):
        move(x, y)
        if (tail_x, tail_y) not in visited:
            visited.append((tail_x, tail_y))

# p1
print(len(visited))

#p2
p = [[0, 0] for _ in range(10)]
visited2 = []
visited2.append(list(p[-1]))

for line in X:
    dir, n = line.split(" ")
    x, y = dirs[dir]
    for _ in range(int(n)):
        move2(x, y)
        if list(p[-1]) not in visited:
            visited2.append(list(p[-1]))

print(len(visited2))

