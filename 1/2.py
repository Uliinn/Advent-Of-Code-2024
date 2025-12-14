from collections import defaultdict

with open("input.txt","r") as f:
  
  list1 = []
  counter_list2 = defaultdict(int)
  for row in f.readlines():
    row = [int(v) for v in row.strip().split()]
    list1.append(row[0])
    counter_list2[row[1]] += 1 #If not seen before, set to 1

  total = 0

  for num in list1:
    total += num * counter_list2[num]
    
  print(total)