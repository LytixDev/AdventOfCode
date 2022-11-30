fish = []
with open("input.txt", "r") as f:
    fish = [int(item) if "\n" not in item else int(item[0:-1]) for item in f.readlines()[0].split(",")]

n = 80
for _ in range(n):
    for i, v in enumerate(fish):
        if v == 0:
            fish[i] = 6
            fish.append(9)
        else:
            fish[i] = v - 1

print(len(fish))
