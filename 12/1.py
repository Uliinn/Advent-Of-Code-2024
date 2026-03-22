


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
    # Perimeter is the number of entered nodes that are not the same symbol
    symbol = grid[y][x]
    currently_visited = set()
    perimeter_count = 0
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
          if (d_x,d_y) in currently_visited: continue
          if not (0 <= d_x < width): # The wall to the left or right
            perimeter_count += 1
            continue
          if not (0 <= d_y < height): # The wall up or down
            perimeter_count += 1
            continue
          stack.append((d_x,d_y))
      

      else:
        perimeter_count += 1

    for visited_x,visited_y in currently_visited:
      visited[visited_y][visited_x] = True

    prices[symbol] += len(currently_visited) * perimeter_count # Area * perimeter

total = 0
for _,price in prices.items():
  total += price 
print(total)