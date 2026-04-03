with open("input.txt","r") as f:
  inp = f.readlines()

  available = list(map(lambda x: x.strip(","),inp[0].split())) # Available towels

  patterns = [v.strip() for v in inp[2:]]

from functools import lru_cache

def is_possible(pattern, towels):
    
    @lru_cache(maxsize=None)
    def dfs(remaining):
        if remaining == "":
            return True
        
        for towel in towels:
            if remaining.startswith(towel):
                if dfs(remaining[len(towel):]):
                   return True
        return False
    
    return dfs(pattern)


possible = 0 
for pattern in patterns:
  possible += is_possible(pattern,available)
print(possible)