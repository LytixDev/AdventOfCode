ASCII_A = 65
ASCII_X = 88


def part_one():
    score = 0
    with open("input.txt", "r") as f:
        for elf, mine in [i.strip("'\n").split(" ") for i in f.readlines()]:
            m = ord(mine) - (ASCII_X - 1)
            score += m
            diff = m - (ord(elf) - (ASCII_A - 1))
            if diff == 0:
                score += 3
            elif diff == -2 or diff == 1:
                score += 6

    print(score) # 11603


def part_two():
    score = 0
    with open("input.txt", "r") as f:
        for elf, mine in [i.strip("'\n").split(" ") for i in f.readlines()]:
            score += (ord(mine) - (ASCII_X)) * 3
            if mine == "Y": # draw
                score += ord(elf) - (ASCII_A - 1)
            elif mine == "Z": # win
                score += (ord(elf) - (ASCII_A - 1)) % 3 + 1
            elif mine == "X": # L
                if ord(elf) - (ASCII_A - 1) == 1:
                    score += 3
                else:
                    score += ord(elf) - (ASCII_A - 1) - 1


    print(score) # 12725


part_one()
part_two()
