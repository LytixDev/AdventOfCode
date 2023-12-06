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

time = int("".join(nums[0]))
dist = int("".join(nums[1]))

ways = 0
for i in range(time):
    t = i * (time - i)
    if t > dist:
        ways += 1

print(ways)
