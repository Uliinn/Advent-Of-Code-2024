

def swap(l, idx1, idx2):
  l[idx1],l[idx2] = l[idx2],l[idx1]


def correctly_ordered(update, rules):
    while True:
        swapped = False
        pages = {}

        for i, page in enumerate(update):
            pages[page] = i

            if page in rules:
                for p in rules[page]:
                    if p in pages:
                        swap(update, pages[p], i)
                        swapped = True
                        break
            if swapped:
                break

        if not swapped:
            return
  
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

  incorrect = [False for i in range(len(updates))]
  
  rule_keys = rules.keys()
  

  for i,update in enumerate(updates):
    pages = set()
    
    for page in update:
      pages.add(page)

      if page in rule_keys:
        valid = True
        for p in rules[page]:
          if p in pages:
            valid = False
        
        if not valid: incorrect[i] = True

    else: # Correct
      # mid_page = update[len(update) // 2]
      # total += mid_page
      pass
  
  # Naive swap until valid
  # Works for this size of inputs
  total = 0

  for i,not_ordered in enumerate(incorrect):
    if not_ordered:
      correctly_ordered(updates[i], rules) # swaps until correctly ordered

      mid_page = updates[i][len(updates[i]) // 2]
      total += mid_page
      

print(total)

