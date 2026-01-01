


with open("input.txt","r") as f:
  
  corrupted_text = "".join([row.strip() for row in f.readlines()])
  
  corrupted_text = list(corrupted_text)
  total = 0

  i = 0
  length = len(corrupted_text)  
  while i < length:
    if "".join(corrupted_text[i:i+4]) == "mul(":
      i += 4
      start = i
      
      while corrupted_text[i].isdigit():
        i += 1
      firstNum = 0
      if corrupted_text[i] == ',' and start != i:
        firstNum = int("".join(corrupted_text[start:i]))
      else:
        continue
      if firstNum >= 1000:
        continue
      i += 1

      start = i
      
      while corrupted_text[i].isdigit():
        i += 1
      secondNum = 0
      if corrupted_text[i] == ')' and start != i:
        secondNum = int("".join(corrupted_text[start:i]))
      else:
        continue
      if secondNum >= 1000:
        continue

      total += firstNum * secondNum
    
    i += 1
  
  print(total)
