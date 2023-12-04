from collections import defaultdict


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
buys = defaultdict(lambda:1)

for i, line in enumerate(l):
    buys[i]
    _, c = line.split(": ")
    win, mine = c.split(" | ")
    win_list = set(str_to_num_list(win))
    mine_list = set(str_to_num_list(mine))
    s = len(set.intersection(win_list, mine_list))
    print(s, buys)
    if s == 0:
        continue
    multiplier = buys[i]
    for j in range(s):
        buys[i + j + 1] += 1 * multiplier


print(buys)
print(sum(buys.values()))

