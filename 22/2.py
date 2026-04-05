# Slow solution, could maybe be optimized further?
import numpy as np

PRUNING_NUMBER = 16777216

with open("input.txt","r") as f:
  start_values = [int(v.strip()) for v in f.readlines()]
  start_values = np.asarray(start_values,dtype = np.int64)


total = 0
n = len(start_values)
prices = np.zeros((n, 2001), dtype=np.int64)
prices[:, 0] = start_values % 10

for i in range(2000):
  # Step 1
  start_values = ((start_values << 6) ^ start_values) % PRUNING_NUMBER
  # Step 2
  start_values = ((start_values >> 5) ^ start_values) % PRUNING_NUMBER
  
  #Step 3
  start_values = ((start_values << 11) ^ start_values) % PRUNING_NUMBER

  prices[:, i+1] = start_values % 10

diffs = np.diff(prices, axis=1)
    
d = diffs + 9
# from [-9,9] to [0,18] so 19 different possible values
keys = d[:, 0:-3] * (19**3) + d[:, 1:-2] * (19**2) + d[:, 2:-1] * 19 + d[:, 3:]
# Get all the 4 tuple values as numbers in 19-base

totals = {}
for buyer in range(n):
    seen = {}
    for j in range(1997): # 4-tuples so gives 2000 minus 3
        k = keys[buyer, j]
        if k not in seen:
            seen[k] = prices[buyer, j+4]
    for k, v in seen.items():
        totals[k] = totals.get(k, 0) + v

print(max(totals.values()))