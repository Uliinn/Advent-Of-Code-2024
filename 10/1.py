

grid = []
nine_coordinates = []
with open("input.txt","r") as f:
  for y,row in enumerate(f.readlines()):
    grid.append([])
    for x,v in enumerate(list(row.strip())):
      val = int(v)
      if val == 9:
        nine_coordinates.append((x,y))
      grid[y].append(val)

width = len(grid[0])
height = len(grid)
#DFS from each 9 down to a zero.
trails = 0
for x_start,y_start in nine_coordinates:
  stack = [(9,x_start,y_start)] # elevation, x, y
  visited_zeroes = set()
  while stack:
    elevation, x, y = stack.pop()

    if elevation == 0 and (x,y) not in visited_zeroes:
      visited_zeroes.add((x,y))
      trails += 1
      continue

    neighbours = [
      (x, y-1), # up
      (x, y+1), # down
      (x-1, y), # left
      (x+1,y)   # right
    ]
    
    for n_x, n_y in neighbours:

      if 0 <= n_y < height and 0 <= n_x < width:

        new_elevation = grid[n_y][n_x]

        if new_elevation + 1 == elevation:
          stack.append((new_elevation,n_x,n_y))

print(trails)

