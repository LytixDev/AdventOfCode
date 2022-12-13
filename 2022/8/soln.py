X = [list(line.strip("\n")) for line in open("input.txt").readlines()]


def is_visible(x, y, x_parent, y_parent, dir):
    if x > len(X) - 1 or y > len(X[0]) - 1 or x < 0 or y < 0:
        return True
    if X[x][y] >= X[x_parent][y_parent]:
        return False

    if dir == "top":
        return is_visible(x - 1, y, x_parent, y_parent, dir)
    elif dir == "bottom":
        return is_visible(x + 1, y, x_parent, y_parent, dir)
    elif dir == "left":
        return is_visible(x, y - 1, x_parent, y_parent, dir)
    else:
        return is_visible(x, y + 1, x_parent, y_parent, dir)


def is_visible_p2(x, y, x_parent, y_parent, dir, depth):
    if x > len(X) - 1 or y > len(X[0]) - 1 or x < 0 or y < 0:
        return depth
    if X[x][y] >= X[x_parent][y_parent]:
        return depth + 1

    if dir == "top":
        return is_visible_p2(x - 1, y, x_parent, y_parent, dir, depth + 1) 
    elif dir == "bottom":
        return is_visible_p2(x + 1, y, x_parent, y_parent, dir, depth + 1) 
    elif dir == "left":
        return is_visible_p2(x, y - 1, x_parent, y_parent, dir, depth + 1) 
    else:
        return is_visible_p2(x, y + 1, x_parent, y_parent, dir, depth + 1) 


p1 = 0
p2 = []
for i in range(1, len(X) - 1):
    for j in range(1, len(X[0]) - 1):
        if (is_visible(i, j - 1, i, j, "left") or is_visible(i, j + 1, i, j, "right") or
            is_visible(i - 1, j, i, j, "top") or is_visible(i + 1, j, i, j, "bottom")):
            p1 += 1
        p2.append(is_visible_p2(i - 1, j, i, j, "top", 0) * is_visible_p2(i, j - 1, i, j, "left", 0)
            * is_visible_p2(i + 1, j, i, j, "bottom", 0) * is_visible_p2(i, j + 1, i, j, "right", 0))

print(len(X[0]) * 4 - 4 + p1)
print(max(p2))
