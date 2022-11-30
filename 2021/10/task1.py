def is_valid(line):
    stack = []
    map = {")": "(", "]": "[", "}": "{", ">": "<"}
    for c in line:
        if c in map:
            if stack and stack[-1] == map[c]:
                stack.pop()
            else:
                return c
        else:
            stack.append(c)
    return ""


with open("input.txt", "r") as f:
    data = [line.strip("\n") for line in f.readlines()]

scores = {")": 3, "]": 57, "}": 1197, ">": 25137, "": 0}
score = 0
for line in data:
    score += scores[is_valid(line)]

print(score)
