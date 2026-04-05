

PRUNING_NUMBER = 16777216

with open("input.txt","r") as f:
  start_values = [int(v.strip()) for v in f.readlines()]


total = 0
for start in start_values:
  secret = start
  for i in range(2000):
    # Step 1
    temp = secret << 6
    secret = secret ^ temp
    secret = secret % PRUNING_NUMBER
    
    # Step 2
    temp = secret >> 5
    secret = secret ^ temp
    secret = secret % PRUNING_NUMBER
    
    #Step 3
    temp = secret << 11
    secret = secret ^ temp
    secret = secret % PRUNING_NUMBER
  
  total += secret
print(total)