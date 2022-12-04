lines = [line.strip("\n") for line in open("input.txt")]
score = 0
PART_ONE = False

for a, b in [line.split(",") for line in lines]:
    # how to unpack the result of split as input to a function?
    A = set(i for i in range(int(a.split("-")[0]), int(a.split("-")[1]) + 1))
    B = set(i for i in range(int(b.split("-")[0]), int(b.split("-")[1]) + 1))
    if not PART_ONE:
        if not A.isdisjoint(B) or not B.isdisjoint(A):
            score += 1
    else:
        if A.issubset(B) or B.issubset(A):
            score += 1

print(score)
