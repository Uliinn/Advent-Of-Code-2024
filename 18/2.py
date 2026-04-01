WIDTH, HEIGHT = 71, 71
GOAL = WIDTH-1, HEIGHT-1

CORRUPTED = 1
SAFE = 0
grid = [[SAFE for x in range(WIDTH)] for y in range(HEIGHT)]
blocks = []
with open("input.txt","r") as f:
  inp = f.readlines()

  for i in range(len(inp)):
    x,y = [int(v) for v in inp[i].strip().split(",")]
    blocks.append((x,y))




# Dijkstra

def dfs(grid,blocks):
  """
  True if there is a path.
  False otherwise
  
  """
  n_safe_spaces = WIDTH * HEIGHT - blocks
  stack = [(0,0)]
  visited = set()

  while stack and len(visited) < n_safe_spaces:

    (x,y) = stack.pop()

    if (x,y) == GOAL:
      return True

    if (x,y) in visited: continue

    visited.add((x,y))

    for xi,yi in [(x+1,y), (x,y-1),(x-1,y),(x,y+1)]:
      if 0 <= xi < WIDTH and 0 <= yi < HEIGHT:
        if grid[yi][xi] == SAFE and (xi,yi) not in visited:
          stack.append((xi,yi))
  return False
        
n_blocks = 0
for (x,y) in blocks:

  grid[y][x] = CORRUPTED
  n_blocks += 1

  if not dfs(grid, n_blocks):
    print(f"{x},{y}")
    break