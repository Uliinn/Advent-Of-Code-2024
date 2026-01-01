# Borrowed from 1, and changed to a temporary changes list
def is_safe(report: list[int]) -> bool:
  changes = []
  for i in range(len(report)-1, 0, -1): 
    changes.append(report[i] - report[i-1])
    
  non_zero_change = all(map(lambda x: x != 0 , changes))
  if not non_zero_change:
    return False
  inc = all(map(lambda x: x > 0 , changes))
  dec = all(map(lambda x: x < 0 , changes))
  if not (dec or inc):
    return False
  min_max_dif = all(map(lambda x: 1 <= abs(x) <= 3 , changes))

  if not min_max_dif:
    return False 
  
  return True

with open("input.txt","r") as f:
  
  reports = [[int(v) for v in row.strip().split()] for row in f.readlines()]

  safe_reports = 0
  
  for report in reports:
    if is_safe(report):
      safe_reports += 1
    else:
      for i in range(len(report)):
        #removing one of the element each iteration
        r = report[:i] + report[i+1:]
        
        if is_safe(r):
          safe_reports += 1
          break


  print(safe_reports)