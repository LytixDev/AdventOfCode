

def part_one():
    s = 0

    with open("input.txt", "r") as f:
        for rucksack in [l.strip('\n') for l in f.readlines()]:
            a, b = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
            common = "".join(set(a).intersection(set(b)))
            s += ord(common) - (96 if ord(common) >= ord("a") else (65 - 27))

    print(s)


def part_two():
    s = 0

    with open("input.txt", "r") as f:
        group = []
        for i, rucksack in enumerate([l.strip('\n') for l in f.readlines()]):
            group.append(rucksack)
            if (i + 1) % 3 != 0:
                continue

            for c in group[0]:
                if c in group[1] and c in group[2]:
                    s += ord(c) - (96 if ord(c) >= ord("a") else (65 - 27))
                    group.clear()
                    break

    print(s)


part_one()
part_two()
