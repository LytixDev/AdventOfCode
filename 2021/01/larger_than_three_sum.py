measurements = []
total = 0

with open("measurement.txt", "r") as f:
    for line in f.readlines():
        measurements.append(int(line))


old = measurements[0]
mid = measurements[1]
new = measurements[2]
prev = (old + mid + new) / 3
for i in measurements[3:]:
    old = mid
    mid = new
    new = i
    current = (old + mid + new) / 3
    if current > prev:
        total += 1

    prev = current


print(total);
