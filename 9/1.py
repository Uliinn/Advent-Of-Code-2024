from collections import deque

  

with open("input.txt","r") as f:
  inp = [[int(v) for v in list(row.strip())]for row in f.readlines()][0] # Gives a list of all integers
  file_blocks = deque() # Stack
  empty_spaces_queue = deque() # Queue

  i = 0
  id = 0
  
  while i + 1 < len(inp):
    file_blocks.extend([id] * inp[i])
    id += 1
    empty_spaces_queue.append(inp[i+1])
    i += 2
  
  # if uneven amount, then an extra file
  if i < len(inp):
    file_blocks.extend([id] * inp[i])
  

  checksum = 0
  pos = 0
  while file_blocks:

    id = file_blocks.popleft()
    
    checksum += id * pos 
    pos += 1

    while file_blocks and file_blocks[0] == id: 
      id = file_blocks.popleft()
      checksum += id * pos 
      pos += 1
    
    if empty_spaces_queue:
      for _ in range(empty_spaces_queue.popleft()):
        if not file_blocks: break
        id = file_blocks.pop()
        checksum += id * pos 
        
        pos += 1
    
  print(checksum)
  






  
    

    







  

