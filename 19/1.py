with open("input.txt","r") as f:
  inp = f.readlines()

  available = list(map(lambda x: x.strip(","),inp[0].split())) # Available towels

  patterns = [list(v.strip()) for v in inp[2:]]




def recursive_is_possible(pattern,towels) -> bool:
  cache = {}
  def _is_possible(pattern,towels,index) -> bool:
    
    if index == len(pattern):
      return True

    for towel in towels:
      if (index,towel) in cache:
        return cache[index,towel] 
      if index + len(towel) > len(pattern): # Towel too long
        continue

      condition = True
      for i,s in enumerate(pattern[index:index + len(towel)]):
        if s != towel[i]:
          condition = False 
          break
      if condition:
        cache[index,towel] = True
        if _is_possible(pattern,towels,index + len(towel)):
          return True
      else:
        cache[index,towel] = False
    return False

  return _is_possible(pattern,towels,0)

possible = 0 
for pattern in patterns:
  if recursive_is_possible(pattern,available):
    possible += 1
print(possible)