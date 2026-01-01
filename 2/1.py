with open("input.txt","r") as f:
  
  reports = [row.strip().split() for row in f.readlines()]

  safe_reports = 0

  for report in reports:

    report = list(map(int, report))



    for i in range(len(report)-1, 0, -1): 
      report[i] = report[i] - report[i-1]
    
    non_zero_change = all(map(lambda x: x != 0 , report[1:]))
    if not non_zero_change:
      continue
    inc = all(map(lambda x: x > 0 , report[1:]))
    dec = all(map(lambda x: x < 0 , report[1:]))
    if not (dec or inc):
      continue
    min_max_dif = all(map(lambda x: 1 <= abs(x) <= 3 , report[1:]))

    if not min_max_dif:
      continue

    safe_reports += 1



  #   if is_safe: safe_reports += 1
  print(safe_reports)