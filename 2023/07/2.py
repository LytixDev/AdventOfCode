from collections import Counter
import heapq

with open("input_proper") as f:
    l = [l.strip().split(" ") for l in f.readlines()]

m = { "A": 14, "K": 13, "Q": 12, "J": 1, "T": 10 }


def get_type(hand):
    c = Counter(hand)
    count = ([0] if (jokers := c.pop("J", 0)) == 5 else sorted(c.values()))
    count[-1] += jokers

    if max(count) > 2:
        return max(count) + 14
    if list(count).count(2) == 2:
        return 2 + 14
    if list(count).count(2) == 1:
        return 1 + 14

    a = [m[char] if not char.isdigit() and char in m else int(char) for char in c.keys()]
    return max(a)


class Schtuk:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)

    def __lt__(self, other):
        a = get_type(self.hand)
        b = get_type(other.hand)
        if a != b:
            return a < b

        for i, j in zip(self.hand, other.hand):
            i = m[i] if not i.isdigit() else int(i)
            j = m[j] if not j.isdigit() else int(j)
            if i != j:
                return i < j


h = []
heapq.heapify(h)
for hand, bid in l:
    s = Schtuk(hand, bid)
    heapq.heappush(h, s)

s = 0
for i, hand in enumerate(h):
    s += hand.bid * (i + 1)

print(s)
