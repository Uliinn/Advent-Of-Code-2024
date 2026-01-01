
with open("input.txt","r") as f:
  
  grid = [list(row.strip()) for row in f.readlines()]
  
  def valid_a_x(y: int,x: int) -> bool:
    
    directions = [(-1,-1),(-1,1),
                  (1,-1),(1,1)]
    
    symbols = []

    for i in range(len(directions)):
      directions[i] = (y + directions[i][0],
                        x + directions[i][1])
      
    for d in directions:
      if not ( 0 <= d[0] < len(grid)):
        return False 
      if not ( 0 <= d[1] < len(grid[0])):
        return False 
    
    symbols = [(grid[directions[0][0]][directions[0][1]], grid[directions[3][0]][directions[3][1]]),
               (grid[directions[1][0]][directions[1][1]], grid[directions[2][0]][directions[2][1]])]
    
    target = ['M', 'S']

    symbols = [sorted(symbols[0]), sorted(symbols[1])]

    if symbols[0] == symbols[1] and symbols[0] == target:
      return True
    return False


  total = 0
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] == 'A':
        
        if valid_a_x(y,x):
          total += 1
        
  
  print(total)


