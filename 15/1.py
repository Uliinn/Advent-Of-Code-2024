
grid = []
moves = []
robot = None

def count(grid): # Just a function to verify correctness
  c = 0
  for row in grid:
    for s in row:
      if s == 'O': c += 1
  return c

with open("input.txt","r") as f:
  
  inp = f.readlines()
  i = 0
  row = inp[0].strip()
  # grid
  while row:
    if '@' in row:
      robot = (row.index('@'),i)
    grid.append(list(row))

    i += 1
    row = inp[i].strip()

  # moves
  i += 1
  for row in inp[i:]:
    moves.extend(row.strip())

def valid_step(grid, robot_pos, direction):
  next_pos = (robot_pos[0] + direction[0], robot_pos[1] + direction[1])
  while True:
    if grid[next_pos[1]][next_pos[0]] == '.':
      return True, next_pos
    elif grid[next_pos[1]][next_pos[0]] == '#':
      return False, None

    next_pos = (next_pos[0] + direction[0], next_pos[1] + direction[1])
  



for move in moves:
  # For viewing the steps
  # for row in grid:
  #   print("".join(row))
  # print("\n\n")
  # print(move)
  direction = None 

  match move:
    case '^':
      direction = (0,-1)
    case '>':
      direction = (1,0)
    case 'v':
      direction = (0,1)
    case '<':
      direction = (-1,0)
  
  is_valid, final_cell = valid_step(grid,robot,direction)
  if is_valid:
    grid[robot[1]][robot[0]] = '.'
    
    grid[robot[1] + direction[1]][robot[0]+ direction[0]] = '@'

    robot = (robot[0] + direction[0], robot[1] + direction[1])

    if direction[1] == 0: # Horisontal
      if direction[0] == 1: # right
        for x in range(robot[0]+1,final_cell[0]+1):
          grid[robot[1]][x] = 'O'
      else: # left
        for x in range(final_cell[0],robot[0]):
          grid[robot[1]][x] = 'O'
    else: # Vertical
      if direction[1] == 1: # down
        for y in range(robot[1]+1,final_cell[1]+1):
            grid[y][robot[0]] = 'O'
      else: # up
          for y in range(final_cell[1],robot[1]):
            grid[y][robot[0]] = 'O'  



total = 0
for y in range(len(grid)):
  for x in range(len(grid[0])):
    if grid[y][x] == 'O':
      total += 100 * y + x


print(total)
