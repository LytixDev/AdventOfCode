def is_valid(line):
    stack = []
    map = {")": "(", "]": "[", "}": "{", ">": "<"}
    for c in line:
        if c in map:
            if stack and stack[-1] == map[c]:
                stack.pop()
            else:
                return None
        else:
            stack.append(c)

    return stack[::-1]


with open("input.txt", "r") as f:
    data = [line.strip("\n") for line in f.readlines()]

points = {"(": 1, "[": 2, "{": 3, "<": 4}
scores = []
for line in data:
    res = is_valid(line)
    if res:
        score = 0
        for add in res:
            score *= 5
            score += points[add]
        scores.append(score)


scores = sorted(scores)
print(scores[len(scores) // 2])

