

with open("input.txt","r") as f:
  
  grid = [list(row.strip()) for row in f.readlines()]
  
  def possible_ways_from_x(y: int,x: int) -> int:
    directions = [(-1,-1),(-1,0),(-1,1),
                  (0,-1),(0,1),
                  (1,-1),(1,0),(1,1)]
    
    total = 0

    for d in directions:
      temp_x = x + d[1]
      temp_y = y + d[0]
      for sym in ['M','A','S']:
        if not (0 <= temp_x < len(grid[0]) and 0 <= temp_y < len(grid)):
          break
        if grid[temp_y][temp_x] != sym:
          break 
        temp_x += d[1]
        temp_y += d[0]
      else:
        total += 1
    
    return total

  num_of_ways = 0
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] == 'X':
        
        
        num_of_ways += possible_ways_from_x(y,x)
        
  
  print(num_of_ways)
