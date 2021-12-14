from collections import Counter

with open("input.txt") as f:
    data = [line.strip("\n").split(" -> ") for line in f.readlines()]

polymer = data[0][0]
pair = {k:v for k, v in data[2:]}

n = 10
for _ in range(n):
    tmp = ""
    for i, char in enumerate(polymer):
        if i == len(polymer) - 1:
            continue
        tmp += char + pair[char + polymer[i+1]]
    polymer = tmp + polymer[-1]
    #print(n, polymer)

count = Counter(polymer)
print(count.most_common(1)[0][1] - count.most_common()[::-1][0][1])
