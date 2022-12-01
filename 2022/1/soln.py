import heapq

def part_one():
    cur = 0
    max = 0

    with open("input.txt", "r") as f:
        for l in f.readlines():
            if l == "\n":
                if cur > max:
                    max = cur
                cur = 0
                continue
            cur += int(l)

    print(max) # 68787


def part_two():
    cur = 0
    # a heap queue would be better, but since there are only 3 items I won't bother
    top3 = [0, 0, 0]

    with open("input.txt", "r") as f:
        for l in f.readlines():
            if l == "\n":
                if cur > top3[0]:
                    top3[0] = cur
                    top3.sort()
                cur = 0
                continue
            cur += int(l)

    print(sum(top3)) # 198041

part_one()
part_two()
