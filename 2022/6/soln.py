X = "".join(line.strip("\n") for line in open("input.txt").readlines())

w = []
for i, c in enumerate(X):
    if len(w) == 14:  # 4 for p1
        print(i)
        break

    if c not in w:
        w.append(c)
    else:
        w = w[w.index(c) + 1:]  # python abstractions brrrrrrrrrrrrr
        w.append(c)
