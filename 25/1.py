import operator


with open("input.txt","r") as f:
  
  inp = [row.strip() for row in f.readlines()]
    
  keys = []

  locks = []


  i = 0
  while i < len(inp):
    is_lock = False
    if '#' in inp[i]: # lock
      is_lock = True
    
    i += 1
    values = [0,0,0,0,0]
    
    for row in inp[i:i+5]:
      r = list(row)
      for idx in range(len(r)):
        if r[idx] == '#':
          values[idx] += 1
    
    if is_lock:
      locks.append(values)
    else:
      keys.append(values)
    i += 7 # 5 for the values, 1 for bottom, 2 to get to the next symbol
  
  working_pairs = 0

  for lock in locks:

    for key in keys:

      combined = map(operator.add, lock, key)

      if all(map(lambda x: x <= 5, combined)):
        working_pairs += 1
  
  print(working_pairs)

  