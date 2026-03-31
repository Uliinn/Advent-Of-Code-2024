# Slow 
# Should be able to replace path tracker for each element in heap to a bitfield instead.
# However, I haven't been able to implement it yet

import heapq
start = None
with open("input.txt","r") as f:
  inp = f.readlines()

  grid = [list(row.strip()) for row in inp]

  for y in range(len(grid)):
    for x in range(len(grid[y])):
      if grid[y][x] == "S":
        
        start = (x,y)

EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


WIDTH = len(grid[0])
HEIGHT = len(grid)

tiles = set()
best_cost = None
heap = [(0,start,EAST,[])] # cost, (x,y), direction
visited = set()
while heap:
  cost, (x,y), direction, path= heapq.heappop(heap)
  if best_cost and cost > best_cost:
    break
  path.append((x,y))
  if grid[y][x] == "E":
    best_cost = cost
    for tile in path:
      tiles.add(tile)
    
  added = 0
  for xi,yi,di in [(x+1,y,EAST), (x,y-1,NORTH),(x-1,y,WEST),(x,y+1,SOUTH)]: #east, north, west, south

    if 0 <= xi < WIDTH and 0 <= yi < HEIGHT and (xi,yi) not in visited and (xi,yi) not in path:
      
      if grid[yi][xi] == "#": # a wall
        continue
      d = abs(di - direction)
      if d == 3: d = 1
      costi = cost + 1 + 1000 * d
      heapq.heappush(heap,(costi,(xi,yi),di,[tile for tile in path])) 
      added += 1
  if added == 0:
    for tile in path:
      visited.add(tile)


print(len(tiles))