with open("input.txt") as f:
    data = [line.strip("\n").split(" -> ") for line in f.readlines()]

#polymer = data[0][0]
pair = {k:v for k, v in data[2:]}
polymer = {}
for i, c in enumerate(data[0][0]):
    if i != len(data[0][0]) - 1:
        polymer[c + data[0][0][i+1]] =  1
polymer[data[0][0][len(data[0][0])-2:]] = 1

n = 40
for _ in range(n):
    tmp = {key:value for key, value in polymer.items()}
    for k, s in polymer.items():
        # decrement current pair
        # add pair to the left of mapped output
        # add pair to the right of mapped outpur
        tmp[k] -= s
        left = k[0] + pair[k]
        right = pair[k] + k[1]
        #print(k, pair[k], left, right, s)
        if left in tmp:
            tmp[left] += s
        else:
            tmp[left] = s

        if right in tmp:
            tmp[right] += s
        else:
            tmp[right] = s
    polymer = {key:value for key, value in tmp.items()}
        

amount = {}
for k, v in polymer.items():
    for i in range(2):
        if k[i] in amount:
            amount[k[i]] += v
        else:
            amount[k[i]] = v

# fix amounts
vals = []
for v in amount.values():
    if v == 0:
        continue
    if v % 2 != 0:
        vals.append((v + 1) // 2)
    else:
        vals.append(v // 2)

print(max(vals) - min(vals))
