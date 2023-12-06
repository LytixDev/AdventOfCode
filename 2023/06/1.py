with open("input_proper", "r") as f:
    l = f.readlines()

l = [ll.split(":")[1].strip("\n") for ll in l]

nums = []
for ll in l:
    n = []
    for lll in ll.split(" "):
        if len(lll) > 0 and lll[0].isdigit():
            n.append(lll)
    nums.append(n)

l = [(int(inner[0]), int(inner[1])) for inner in zip(*nums)]


s = 1
for time, dist in l:
    # brute force
    ways = 0
    for i in range(time):
        t = i * (time - i)
        if t > dist:
            ways += 1
    s *= ways

print(s)
