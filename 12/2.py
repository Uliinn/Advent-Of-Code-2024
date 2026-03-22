


grid = []
prices = {}
with open("input.txt","r") as f:
  for row in f.readlines():
    grid_row = []
    for symbol in list(row.strip()):
      grid_row.append(symbol)
      if symbol not in prices:
        prices[symbol] = 0
    grid.append(grid_row)

width = len(grid[0])
height = len(grid)

visited = [[False for i in range(width)] for j in range(height)]

for y in range(height):
  for x in range(width):

    if visited[y][x]:
      continue

    
    # DFS
    # Area is size of currently_visited

    symbol = grid[y][x]
    currently_visited = set()
    stack = [(x,y)]
    
    while stack:
      current_x, current_y = stack.pop()
      
      if grid[current_y][current_x] == symbol:

        if (current_x,current_y) in currently_visited:
          continue
        currently_visited.add((current_x,current_y))

        directions = [
          (current_x,current_y-1), # up
          (current_x,current_y+1), # down
          (current_x-1,current_y), # left
          (current_x+1,current_y) # right
        ]

        for d_x,d_y in directions:
          if (d_x,d_y) in currently_visited: # Already visited
            continue
          if not (0 <= d_x < width): # The wall to the left or right
            continue
          if not (0 <= d_y < height): # The wall up or down
            continue
          stack.append((d_x,d_y))

    for visited_x,visited_y in currently_visited:
      visited[visited_y][visited_x] = True


    side_count = 0
    # As many corners as there are sides in a 2d polygon
    # For each cell, look at its 4 corners.
    # Every corner is definied by its to side neighbours (n1, n2) and a diagonal
    # Outwards corner: n1 and n2 is outside of the area
    # Inwards corner: n1 and n2 is inside the area, but the diagonal is outside
    neighbour_pairs = [
        ( 0, -1,  1,  0),  # top-right
        ( 1,  0,  0,  1),  # bottom-right
        ( 0,  1, -1,  0),  # bottom-left
        (-1,  0,  0, -1),  # top-left
      ]
    
    for (cx, cy) in currently_visited:
      for (dx1, dy1, dx2, dy2) in neighbour_pairs:

        n1 = (cx + dx1, cy + dy1) in currently_visited
        n2 = (cx + dx2, cy + dy2) in currently_visited
        diag = (cx + dx1 + dx2, cy + dy1 + dy2) in currently_visited

        if not n1 and not n2:      # Outwards corner
          side_count += 1
        elif n1 and n2 and not diag:  # Inwards corner
          side_count += 1

    prices[symbol] += len(currently_visited) * side_count

total = 0
for _,price in prices.items():
  total += price 
print(total)