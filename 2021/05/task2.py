points = []
with open("input.txt", "r") as f:
    points = [[line.split(" -> ")[0].split(","), line.split(" -> ")[1][0:-1].split(",")] for line in f.readlines()]


# key -> "x,y"
# val -> times overlapped by line
map = {}

for point in points:
    x_1, y_1 = point[0]
    x_2, y_2 = point[1]
    # wish I could do this more gracefully !
    x_1 = int(x_1)
    x_2 = int(x_2)
    y_1 = int(y_1)
    y_2 = int(y_2)
    
    # could make this if else clause into a function to minimize code overlap
    # create vertical line
    if x_1 == x_2:
        min_y = min(y_1, y_2)
        max_y = max(y_1, y_2)
        for i in range(max_y - min_y + 1):
            key = str(x_1) + "," + str(min_y + i)
            if key in map:
                map[key] += 1
            else:
                map[key] = 1

    # create horisontal line
    elif y_1 == y_2:
        min_x = min(x_1, x_2)
        max_x = max(x_1, x_2)
        for i in range(max_x - min_x + 1):
            key = str(min_x + i) + "," + str(y_1)
            if key in map:
                map[key] += 1
            else:
                map[key] = 1
    
    # create diagonal line
    else:
        start_x = x_1 < x_2
        start_y = y_1 < y_2

        for i in range(abs(x_2 - x_1) + 1):
            if start_x:
                new_x = str(x_1 + i)
            else:
                new_x = str(x_1 - i)
            if start_y:
                new_y = str(y_1 + i)
            else:
                new_y = str(y_1 - i)

            key = new_x + "," + new_y
            if key in map:
                map[key] += 1
            else:
                map[key] = 1


total_over_2 = 0
for val in map.values():
    if val >= 2:
        total_over_2 += 1

print(total_over_2)
