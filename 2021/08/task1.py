# Advent of Parsing Text :////

tmp = []
data = []
with open ("input.txt", "r") as f:
    for line in f.readlines():
        #tmp.append(line[line.find("|")+1][-1])
        tmp.append(line[61:-1])

for entry in tmp:
    for item in entry.split(" "):
        data.append(item)

unique_lengths = [2, 3, 4, 7]
sum = 0
for digits in data:
    if len(digits) in unique_lengths:
        sum += 1

print(sum)
