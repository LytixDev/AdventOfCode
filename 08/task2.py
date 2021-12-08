def get_num(o, one, four, seven):

    if len(o) == 2:
        return 1
    if len(o) == 4:
        return 4
    if len(o) == 3:
        return 7
    if len(o) == 7:
        return 8

    if len(o) == 6: # distinguish between 0, 6 and 9
        if len(o.difference(one)) == 5:
            return 6
        if len(o.difference(four)) == 2:
            return 9
        if len(o.difference(four)) == 3:
            return 0

    if len(o) == 5: # differentiate between 2, 3 and 5
        if len(o.difference(one)) == 3:
            return 3
        if len(o.intersection(four)) == 3:
            return 5
        if len(o.intersection(four)) == 2:
            return 2

    return -1


def soln(data):
    total = 0

    for line in data:
        all = line.replace(" | ", " ").split(" ")
        inp = line.partition(" | ")[0].split(" ")
        outp = line.partition(" | ")[2].split(" ")

        one = four = seven = set()

        for i in all:
            if len(i) == 2:
                one = set(list(i))
            if len(i) == 4:
                four = set(list(i))
            if len(i) == 3:
                seven = set(list(i))
        num = ""
        # due to the nature of the output there will always be a one, a four, and a seven
        for o in outp:
            num += str(get_num(set(list(o)), one, four, seven))
        total += int(num)
    return total


with open('input.txt') as f:
    data = f.readlines()
    data = [i.strip() for i in data]
    t = soln(data)
    print(t)
