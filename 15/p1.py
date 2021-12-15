import heapq
from collections import defaultdict

with open("input.txt", "r") as f:
    data = [[int(point) for point in line.strip("\n")] for line in f.readlines()]


start = (0, 0)
N = len(data)
M = len(data[0])
cost = defaultdict(int)

# priority queue
pq = [(0, 0, 0)]
heapq.heapify(pq)
visited = set()

while len(pq) > 0:
    c, row, col = heapq.heappop(pq)

    if (row, col) in visited:
        continue

    visited.add((row, col))
    cost[(row, col)] = c

    if row == N - 1 and col == M - 1:
        break

    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        rr = row + dr
        cc = col + dc
        if not (0 <= rr < N and 0 <= cc < M):
            continue

        heapq.heappush(pq, (c + data[rr][cc], rr, cc))

print(cost[(N - 1, M - 1)])
