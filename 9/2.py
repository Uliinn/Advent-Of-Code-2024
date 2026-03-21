

"""
Not n^2, doesn't work

But there are only 10 different space sizes
heap? map?

map int 1-9 (the space sizes) and there are heaps with the lowest position.

if the next file is e.g. size 5, then check the lowest index for sizes 5 - 9 and the original index and take the lowest one.
It disappears and a new spot replaces it (if the spot isn't size 5), and ends up at index + 5
When it "lands" there, just add to the checksum directly.

files are stored as a tuple with (id, index_start, length)
empty spaces in a map of 9 heaps (1-9) with key: size, and the values in the min-heap the indexes.

"""

import heapq as hq
from collections import deque, defaultdict

with open("input.txt","r") as f:
  inp = [[int(v) for v in list(row.strip())]for row in f.readlines()][0] # Gives a list of all integers
  file_blocks = deque() # Stack
  empty_spaces_map = defaultdict(list) # Map of Heaps

  i = 0
  id = 0
  pos = 0
  
  while i + 1 < len(inp):
    file_blocks.append((id,pos,inp[i]))
    pos += inp[i]
    id += 1

    size_of_free_space = inp[i+1]

    hq.heappush(empty_spaces_map[size_of_free_space],pos)
    pos += size_of_free_space
    i += 2
  
  # if uneven amount, then an extra file
  if i < len(inp):
    file_blocks.append((id,pos,inp[i]))
  
  checksum = 0

  while file_blocks:
    id, start_pos, length = file_blocks.pop()

    index_length = None
    for i in range(length,10): # from length to 9, to see which gives the earliest
      if empty_spaces_map[i] and empty_spaces_map[i][0] < start_pos:
        start_pos = empty_spaces_map[i][0]
        index_length = i
    
    if index_length:
      hq.heappop(empty_spaces_map[index_length])
      if index_length != length:
        hq.heappush(empty_spaces_map[index_length - length],start_pos + length)
    
    checksum += (id * (2*start_pos + length - 1 ) * length) // 2
  
  print(checksum)
        