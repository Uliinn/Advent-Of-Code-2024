import numpy as np
PRUNING_NUMBER = 16777216

with open("input.txt","r") as f:
  start_values = [int(v.strip()) for v in f.readlines()]
  start_values = np.asarray(start_values,dtype = np.int64)


total = 0

for i in range(2000):
  # Step 1
  start_values = ((start_values << 6) ^ start_values) % PRUNING_NUMBER
  # Step 2
  start_values = ((start_values >> 5) ^ start_values) % PRUNING_NUMBER
  
  #Step 3
  start_values = ((start_values << 11) ^ start_values) % PRUNING_NUMBER

    
  
  
print(sum(start_values))