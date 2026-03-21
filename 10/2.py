
#Only difference from 1 is I removed the visited_zeroes

grid = []
nine_coordinates = []
with open("input.txt","r") as f:
  for y,row in enumerate(f.readlines()):
    grid.append([])
    for x,v in enumerate(list(row.strip())):
      val = int(v)
      if val == 9:
        nine_coordinates.append((y,x))
      grid[y].append(val)

width = len(grid[0])
height = len(grid)
#DFS from each 9 down to a zero.
trails = 0
for y_start,x_start in nine_coordinates:
  stack = [(9,y_start,x_start)] # elevation, y, x
  while stack:
    elevation, y, x = stack.pop()

    if elevation == 0:
      trails += 1
      continue

    neighbours = [
      (y-1, x), # up
      (y+1, x), # down
      (y, x-1), # left
      (y,x+1)   # right
    ]
    
    for n_y, n_x in neighbours:

      if 0 <= n_y < height and 0 <= n_x < width:

        new_elevation = grid[n_y][n_x]

        if new_elevation + 1 == elevation:
          stack.append((new_elevation,n_y,n_x))

print(trails)

