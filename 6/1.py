import time

def step(pos,direction): return (pos[0]+direction[0],pos[1]+direction[1])
t = time.time()
for i in range(1):
  with open("input.txt","r") as f:
    
    grid = [list(row.strip()) for row in f.readlines()]

    distinct_cells = set()

    directions = [ # Always 90 degrees right turn, index += 1
      (-1,0), # up (starting position)
      (0,1), # right
      (1,0), # down
      (0,-1) # left
    ] # y,x

    current_direction_idx = 0

    y,x = -1,-1

    for yi in range(len(grid)):
      for xi in range(len(grid[0])):
        if grid[yi][xi] == '^': # starting position
          y,x = yi,xi
          grid[yi][xi] = "." # Remove this unique char
    
    distinct_cells.add((y,x))

    y_max = len(grid)
    x_max = len(grid[0])

    while True:

      yi,xi = step((y,x),directions[current_direction_idx])

      if yi < 0 or yi >= y_max:
        break 
      if xi < 0 or xi >= x_max:
        break
      
      next_cell = grid[yi][xi]

      if next_cell == "#":
        current_direction_idx = (current_direction_idx + 1) % 4 # loop around direction list
        # Don't save obstacle position. Next iteration the direction has only changed

      elif next_cell == ".":
        distinct_cells.add((yi,xi))
        y,x = yi,xi
      else:
        raise RuntimeError("next_cell neither '.' or '#'")
        
    print(len(distinct_cells))



