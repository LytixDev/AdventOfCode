with open("input.txt", "r") as f:
    # make input as 2d list
    map = [[int(i) for i in line[:-1]] for line in f.readlines()]

rows = len(map)
cols = len(map[0])
ans = 0

# look at any point and check if smaller neighbour exists 
for row in range(rows):
    for col in range(cols):
        low = True
        # where we want to look
        # rr and cc represent x and y coordinates of where we are looking
        for dd in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            rr = row + dd[0]
            cc = col + dd[1]

            # check if we are looking outside of the map
            if not ((0 <= rr and rr < rows) and (0 <= cc and cc < cols)):
                continue
            
            if map[rr][cc] <= map[row][col]:
                low = False
                break

        if low:
            ans += map[row][col] + 1

print(ans)
