# My own problem

# Now, how many different ways can we spell XMAS, in any way?
# For example
# .S.
# AM.
# ..X

# So it doesnt need to be in one direction, but can change at anytime


with open("input.txt","r") as f:
  
  grid = [list(row.strip()) for row in f.readlines()]
  mem = {}
  def possible_ways_from(symbol: str,y: int,x: int) -> int:
    if symbol == 'S': return 1

    if (symbol,y,x) in mem.keys():
      return mem[(symbol,y,x)]
    target = ''
    match symbol:
      case 'X':
        target = 'M'
      case 'M':
        target = 'A'
      case 'A':
        target = 'S'
    
    directions = [(-1,-1),(-1,0),(-1,1),
                  (0,-1),(0,1),
                  (1,-1),(1,0),(1,1)]
    total = 0

    for d in directions:
      new_y,new_x = y+d[0], x+d[1]

      new_y = min(max(new_y,0),len(grid)-1)
      new_x = min(max(new_x,0),len(grid[0])-1)

      if grid[new_y][new_x] == target:
        total += possible_ways_from(target,new_y,new_x)

    mem[(symbol,y,x)] = total
    return total

  num_of_ways = 0
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] == 'X':
        num_of_ways += possible_ways_from('X',y,x)
        
  
  print(num_of_ways)
