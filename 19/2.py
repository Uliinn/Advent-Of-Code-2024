with open("input.txt","r") as f:
  inp = f.readlines()

  available = list(map(lambda x: x.strip(","),inp[0].split())) # Available towels

  patterns = [v.strip() for v in inp[2:]]


from functools import lru_cache

def count_ways(pattern, towels):
    
    @lru_cache(maxsize=None)
    def dfs(remaining):
        if remaining == "":
            return 1
        
        total = 0
        for towel in towels:
            if remaining.startswith(towel):
                total += dfs(remaining[len(towel):])
        return total
    
    return dfs(pattern)


possible = 0 
for pattern in patterns:
  possible += count_ways(pattern,available)
print(possible)


