with open("input") as f:
    l = [line.strip("\n") for line in f.readlines()]


total = 0
for line in l:
    # slow but works
    line = (
        line.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
    )

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
