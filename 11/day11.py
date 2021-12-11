def step(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j] += 1
                # flash neighbours
                #for k in range(-1, 2):
                #    for l in range(-1, 2):
                #        if len(data) > k >= 0 and len(data[0]) > l >= 0:
                #            data[k][l] += 1
    

def step_neighbour(data, x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_x = x + i
            new_y = y + j

            if len(data) > new_x >= 0 and len(data[0]) > new_y >= 0:
                if data[new_x][new_y] != 0:
                    data[new_x][new_y] += 1


def flash(data):
    finished = True
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] > 9:
                finished = False
                c[0] += 1
                data[i][j] = 0
                step_neighbour(data, i, j)

    if not finished:
        flash(data)

    for i in data:
        for j in i:
            if j != 0:
                return False
    return True


with open("input.txt", "r") as f:
    data = [[int(i) for i in line.strip("\n")] for line in f.readlines()]

n = 100
c = [0]

for i in range(n):
    step(data)
    flash(data)

finished = False
i = 0
while not finished:
    i += 1
    step(data)
    finished = flash(data)

print("task1: ", c[0])
print("task2: ", i + 100)

