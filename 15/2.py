
grid = []
moves = []
robot = None

with open("input.txt","r") as f:
  
  inp = f.readlines()
  i = 0
  row = inp[0].strip()
  # grid
  while row:

    new_row = []
    for s in row:
      if s == '@':
        new_row.extend("@.")
      elif s == ".":
        new_row.extend("..")
      elif s == "#":
        new_row.extend("##")
      elif s == "O":
        new_row.extend("[]")
      
    row = new_row
    if '@' in row:
      robot = (row.index('@'),i)
    grid.append(list(row))

    i += 1
    row = inp[i].strip()

  # moves
  i += 1
  for row in inp[i:]:
    moves.extend(row.strip())


def valid_step(grid, pos, direction): # Now only handles horisontal
  next_pos = (pos[0] + direction[0], pos[1])
  while True:
    if grid[next_pos[1]][next_pos[0]] == '.':
      return True, next_pos
    elif grid[next_pos[1]][next_pos[0]] == '#':
      return False, None

    next_pos = (next_pos[0] + direction[0], next_pos[1])
  


def get_boxes_to_move(grid, pos, direction): # Returns a set of all the positions that needs to be moves, or None if blocked
    
    next_pos = (pos[0], pos[1] + direction[1])
    cell = grid[next_pos[1]][next_pos[0]]
    
    if cell == '#':
        return None
    if cell == '.':
        return set()
    
    if cell == '[':
        box_positions = {next_pos, (next_pos[0]+1, next_pos[1])}
    else:  # ']'
        box_positions = {next_pos, (next_pos[0]-1, next_pos[1])}
    
    all_to_move = set(box_positions)
    for bp in box_positions:
        sub = get_boxes_to_move(grid, bp, direction)
        if sub is None:
            return None
        all_to_move |= sub
    
    return all_to_move


for move in moves:
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

    if direction[1] == 0:  # Horisontal as in part 1
        is_valid, final_cell = valid_step(grid, robot, direction)
        if is_valid:
            # Move all between robot and final step, one step
            rx, ry = robot
            dx = direction[0]
            
            x = final_cell[0]
            while x != rx:
                grid[ry][x] = grid[ry][x - dx]
                x -= dx
            grid[ry][rx] = '.'
            robot = (rx + dx, ry)

    else:  # Vertical
        to_move = get_boxes_to_move(grid, robot, direction)
        if to_move is not None:
            # Save content, remove them from grid, write to new cells
            saved = {pos: grid[pos[1]][pos[0]] for pos in to_move}

            for pos in to_move:
                grid[pos[1]][pos[0]] = '.'
            
            for pos, ch in saved.items():
                new_pos = (pos[0], pos[1] + direction[1])
                grid[new_pos[1]][new_pos[0]] = ch
            
            grid[robot[1]][robot[0]] = '.'
            robot = (robot[0], robot[1] + direction[1])
            grid[robot[1]][robot[0]] = '@'


total = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '[':
            total += 100 * y + x

print(total)