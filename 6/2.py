
# Graph problem
# Find where we can add one obstacle to create a cycle
# We check if each of the distinct cells create a cycle if it gets replaced with an obstacle
# A cycle can be detected when the guard enters a previous visited cell, in the same direction

# Obstacle set instead of 2d grid
# No step function

# Could surely be improved by "teleporting" the guard between each obstacle instead of stepping one at a time

with open("input.txt", "r") as f:
  grid = [list(row.strip()) for row in f.readlines()]
  y_max = len(grid)
  x_max = len(grid[0])

  directions = [(-1,0), (0,1), (1,0), (0,-1)]

  start_y, start_x = -1, -1
  obstacles = set()

  for yi in range(y_max):
    for xi in range(x_max):
      if grid[yi][xi] == '^':
        start_y, start_x = yi, xi
      elif grid[yi][xi] == '#':
        obstacles.add((yi, xi))

  distinct_cells = set()
  y, x = start_y, start_x
  dir_idx = 0
  distinct_cells.add((y, x))

  while True:
    dy, dx = directions[dir_idx]
    yi, xi = y + dy, x + dx

    if yi < 0 or yi >= y_max or xi < 0 or xi >= x_max:
      break

    if (yi, xi) in obstacles:
      dir_idx = (dir_idx + 1) % 4
    else:
      distinct_cells.add((yi, xi))
      y, x = yi, xi

  distinct_cells.discard((start_y, start_x))

  cycles = 0

  for obs_y, obs_x in distinct_cells:
    obstacles.add((obs_y, obs_x))

    y, x = start_y, start_x
    dir_idx = 0
    visited = set()

    while True:
      dy, dx = directions[dir_idx]
      yi, xi = y + dy, x + dx

      if yi < 0 or yi >= y_max or xi < 0 or xi >= x_max:
        break

      if (yi, xi) in obstacles:
        dir_idx = (dir_idx + 1) % 4
      else:
        state = (yi, xi, dir_idx)
        if state in visited:
          cycles += 1
          break
        visited.add(state)
        y, x = yi, xi

    obstacles.discard((obs_y, obs_x))

  print(cycles)