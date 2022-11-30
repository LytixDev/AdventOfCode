import pygame

# constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WIDTH = HEIGHT = 1000
ROWS = COLS = 100
PIXEL_SIZE = WIDTH // ROWS


def init_grid(rows, cols):
    # inititalize grid of all zeros, i.e all white
    grid = []
    
    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(WHITE)

    return grid


def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            #pixel = WHITE if pixel == 0 else BLACK
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))


def draw(win, grid):
    draw_grid(win, grid)
    pygame.display.update()


def add_grid(x, y, color):
    grid[x][y] = color
    draw(WIN, grid)


def main():
    pygame.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Paint")
    grid = init_grid(ROWS, COLS)
    
    running = True
    clock = pygame.time.Clock()
    # main event loop
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw(WIN, grid)
    
    # take a screenshot of the surface before exiting
    pygame.image.save(WIN, "drawn_picture.png")
    pygame.quit()


def find_local_minimum():
    local_minimums = []
    for row in range(rows):
        for col in range(cols):
            local = True
            for dd in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                rr = row + dd[0]
                cc = col + dd[1]

                if not ((0 <= rr and rr < rows) and (0 <= cc and cc < cols)):
                    continue
                
                if map[rr][cc] <= map[row][col]:
                    local = False
                    break

            if local:
                local_minimums.append([row, col])
                add_grid(row, col, BLUE)

    
    return local_minimums


def get_neighbours(x, y):
    neighbours = []
    for dd in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        nx = x + dd[0]
        ny = y + dd[1]
        if rows > nx >= 0 and cols > ny >= 0:
            if map[nx][ny] != 9:
                neighbours.append([nx, ny])
            elif map[nx][ny] == 9:
                add_grid(nx, ny, BLACK)

    return neighbours

    
def dfs(x, y, c):
    if (x, y) not in visited:
        visited.add((x, y))
        add_grid(x, y, (0, 255- (9 - map[x][y]) * 15, 0))
        for neighbour in get_neighbours(x, y):
            dfs(neighbour[0], neighbour[1], c)
    


with open("input.txt", "r") as f:
    # make input as 2d list
    map = [[int(i) for i in line[:-1]] for line in f.readlines()]

rows = len(map)
cols = len(map[0])
basin_lens = []

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")
grid = init_grid(ROWS, COLS)


for x, y in find_local_minimum():
    visited = set()
    dfs(x, y, 0)
    basin_lens.append(len(visited))

b = sorted(basin_lens)[::-1]
print(b[0] * b[1] * b[2])

pygame.image.save(WIN, "drawn_picture.png")
pygame.quit()
