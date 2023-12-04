with open("input") as f:
    l = [line.strip("\n") for line in f.readlines()]


def str_to_num_list(s):
    l = []
    for n in s.split(" "):
        try:
            l.append(int(n))
        except:
            pass

    return l


p = 0
for line in l:
    _, c = line.split(": ")
    win, mine = c.split(" | ")
    win_list = set(str_to_num_list(win))
    mine_list = set(str_to_num_list(mine))
    s = len(set.intersection(win_list, mine_list))
    if s != 0:
        p += 2 ** (s - 1)

print(p)
