with open("input") as f:
    l = [line.strip("\n") for line in f.readlines()]


total = 0
for line in l:
    for c in line:
        if c >= '0' and c <= '9':
            total += int(c) * 10
            break
    # from behind
    for c in line[::-1]:
        if c >= '0' and c <= '9':
            total += int(c)
            break

print(total)
