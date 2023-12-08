from collections import Counter
import heapq

with open("input") as f:
    l = [l.strip().split(" ") for l in f.readlines()]



class Schtuk:
    def __init__(self, hand, bid):
        self.m = { "A": 14, "K": 13, "Q": 12, "J": 11, "T": 10 }
        self.hand = hand
        self.bid = int(bid)

    def get_type(self):
        c = Counter(self.hand)
        count = c.values()
        if max(count) > 2:
            return max(count) + 14
        if list(count).count(2) == 2:
            return 2 + 14
        if list(count).count(2) == 1:
            return 1 + 14
        a = [self.m[char] if not char.isdigit() else int(char) for char in c.keys()]
        return max(a)

    def __lt__(self, other):
        a = self.get_type()
        b = other.get_type()
        if a != b:
            return a < b

        for i, j in zip(self.hand, other.hand):
            i = self.m[i] if not i.isdigit() else int(i)
            j = self.m[j] if not j.isdigit() else int(j)
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
