import heapq

with open("input.txt","r") as f:
  

  list1 = []
  list2 = []
  for row in f.readlines():
    row = [int(v) for v in row.strip().split()]
    heapq.heappush(list1,row[0])
    heapq.heappush(list2,row[1])
  
  total = 0

  while list1:
    a,b = heapq.heappop(list1), heapq.heappop(list2)

    total += abs(a-b)  
    
  print(total)