
# Was linear search, but can be binary search

WIDTH, HEIGHT = 71, 71
GOAL = WIDTH-1, HEIGHT-1

block_to_time = dict()
time_to_block = dict()
with open("input.txt","r") as f:
  inp = f.readlines()

  for i in range(len(inp)):
    x,y = [int(v) for v in inp[i].strip().split(",")]
    block_to_time[(x,y)] = i
    time_to_block[i] = (x,y)


blocks = block_to_time.keys()

# Dijkstra

def dfs(k,blocks, blocks_to_time):
  """
  True if there is a path.
  False otherwise
  
  """
  def block_present(x,y):
    if (x,y) not in blocks:
      return False 
    
    return blocks_to_time[(x,y)] <= k
      
  stack = [(0,0)]
  visited = set()

  while stack:

    (x,y) = stack.pop()

    if (x,y) == GOAL:
      return True

    if (x,y) in visited: continue

    visited.add((x,y))

    for xi,yi in [(x+1,y), (x,y-1),(x-1,y),(x,y+1)]:
      if 0 <= xi < WIDTH and 0 <= yi < HEIGHT:
        if  not block_present(xi,yi) and (xi,yi) not in visited:
          stack.append((xi,yi))
  return False
        

lo, hi = 0, len(blocks)
earliest_block = None
while lo < hi:
  k = lo + ((hi - lo) // 2)

  if not dfs(k,blocks,block_to_time):
    earliest_block = time_to_block[k]
    hi = k
  else:
    lo = k + 1

print(earliest_block)