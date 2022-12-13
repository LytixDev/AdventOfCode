X = [line.strip("\n") for line in open("input.txt").readlines()]

instructions = {"noop": 1, "addx": 2}
x = 1
cycles = 0
s = 0

for instruction in X:
    for _ in range(instructions[instruction[0:4]]):
        cycles += 1
        if cycles % 40 == 20:
            s += cycles * x

    if instruction[0:4] == "addx":
        x += int(instruction[5:])

print(s)

