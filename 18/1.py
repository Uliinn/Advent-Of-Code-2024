import heapq

n_bytes = 1024

WIDTH, HEIGHT = 71, 71

CORRUPTED = 1
SAFE = 0
grid = [[SAFE for x in range(WIDTH)] for y in range(HEIGHT)]

with open("input.txt","r") as f:
  inp = f.readlines()

  for i in range(n_bytes):
    x,y = [int(v) for v in inp[i].strip().split(",")]
    grid[y][x] = CORRUPTED



n_safe_spaces = WIDTH * HEIGHT - n_bytes
heap = [(0,(0,0))]
visited = set()
# Dijkstra
GOAL = WIDTH-1, HEIGHT-1

while heap and len(visited) < n_safe_spaces:

  cost, (x,y) = heapq.heappop(heap)

  if (x,y) == GOAL:
    print(cost)
    break

  if (x,y) in visited: continue

  visited.add((x,y))

  for xi,yi in [(x+1,y), (x,y-1),(x-1,y),(x,y+1)]:
    if 0 <= xi < WIDTH and 0 <= yi < HEIGHT:
      if grid[yi][xi] == SAFE and (xi,yi) not in visited:
        heapq.heappush(heap,(cost + 1, (xi,yi)))
      


