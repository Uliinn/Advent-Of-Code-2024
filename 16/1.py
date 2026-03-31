
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

heap = [(0,start,EAST)] # cost, (x,y), direction
visited = set()
while heap:
  cost, (x,y), direction= heapq.heappop(heap)

  if grid[y][x] == "E":
    print(cost)
    break

  visited.add((x,y))

  for xi,yi,di in [(x+1,y,EAST), (x,y-1,NORTH),(x-1,y,WEST),(x,y+1,SOUTH)]: #east, north, west, south

    if 0 <= xi < WIDTH and 0 <= yi < HEIGHT and (xi,yi) not in visited:
      
      if grid[yi][xi] == "#": # a wall
        continue
      d = abs(di - direction)
      if d == 3: d = 1
      costi = cost + 1 + 1000 * d
      heapq.heappush(heap,(costi,(xi,yi),di)) 


