


with open("input.txt","r") as f:
  
  inp = [row.strip() for row in f.readlines()]
  
  rules = {}

  i = 0

  while True:
    if not inp[i]:
      i += 1
      break

    rule = inp[i].split('|')

    key = int(rule[0])
    val = int(rule[1])

    if key in rules.keys():
      rules[key].append(val)
    else:
      rules[key] = [val]
    
    i += 1
  
  updates = [[int(v) for v in update.split(',')] for update in inp[i:]]

  
  rule_keys = rules.keys()
  total = 0

  for update in updates:
    pages = set()
    
    for page in update:
      pages.add(page)

      if page in rule_keys:
        valid = True
        for p in rules[page]:
          if p in pages:
            valid = False
        
        if not valid: break

    else:
      mid_page = update[len(update) // 2]
      total += mid_page

print(total)





# Sätt in i en dictionary med X -> Y 

# Loopa igenom pages och lägg till i ett set, och ifall den finns i dictionaryn, kolla ifall värdet finns i setet redan. isåfall
