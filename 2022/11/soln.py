import re
import math

binary_expression = {"+": lambda x, y: x + y,
                     "-": lambda x, y: x - y,
                     "*": lambda x, y: x * y,
                     "/": lambda x, y: x / y}
part_one = False
lcm = 1


# oop bad
class Monke:
    def __init__(self, items: list, operand, op_val, test_val, true_path, false_path):
        self.items = items
        self.operand = operand
        self.op_val = op_val
        self.test_val = test_val
        self.true_path = true_path
        self.false_path = false_path

    def process(self) -> tuple[int, int]:
        # returns a tuple containing the items worry level and which monkey its thrown to
        old = self.items.pop(0)
        if type(self.op_val) == str:
            new = binary_expression[self.operand](old, old)
        else:
            new = binary_expression[self.operand](old, self.op_val)

        if part_one:
            new //= 3
        else:
            new %= lcm

        if new % self.test_val == 0:
            new = self.test_val
            return (new, self.true_path)
        else:
            return (new, self.false_path)

    def add_item(self, item):
        self.items.append(item)

    def __repr__(self):
        return f"Monke(items={self.items}, operand={self.operand}, op_val={self.op_val},\
 test_val={self.test_val}, true_path={self.true_path}, false_path={self.false_path})"


def parse_monke(monke_input):
    global lcm
    monkes = []
    divisors = []
    with open(monke_input) as f:
        for monke_raw in f.read().split("\n\n"):
            monke_lines = monke_raw.split("\n")
            items = [int(s) for s in re.findall(r"\d+", monke_lines[1])]
            operand, op_val = monke_lines[2].split()[-2:]
            try:
                op_val = int(op_val)
            except:
                pass # lol
            test_val = int(monke_lines[3].split()[-1])
            true_path = int(monke_lines[4].split()[-1])
            false_path = int(monke_lines[5].split()[-1])
            monkes.append(Monke(items, operand, op_val, test_val, true_path, false_path))
            divisors.append(test_val)

    lcm = math.lcm(*divisors)
    return monkes


monkes = parse_monke("dummy.txt")
n = [0 for _ in range(len(monkes))]

for _ in range(20 if part_one else 10000):
    for i, monke in enumerate(monkes):
        while monke.items:
            n[i] += 1
            item, receiver = monke.process()
            monkes[receiver].add_item(item)

n.sort(reverse=True)
print(n)
print(n[0] * n[1])
