with open("input_proper") as f:
    d = [l.strip() for l in f.readlines()]

# brute force
s = 0
for l in d:
    values = [int(v) for v in l.split(" ")]
    a = [values]
    while True:
        if a[-1].count(0) == len(a[-1]):
            a.pop()
            break
        A = []
        for idx in range(len(a[-1]) - 1):
            i, j = a[-1][idx:idx+2]
            A.append(j - i)
        a.append(A)

    pred = 0
    for A in a[::-1]:
        pred = A[0] - pred
    s += pred

print(s)
