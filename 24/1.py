


variables = {}

highest_zs = 0

with open("input.txt","r") as f:
  inp = f.readlines()
  i = 0
  while inp[i] != "\n":
    var, val = inp[i].split()
    variables[var[:-1]] = int(val) # remove :
    i += 1
  
  statements = [[v for v in row.strip().split()] for row in inp[i+1:]]

  for _,_,_,_,ans in statements:
    if "z" in ans and highest_zs < int(ans[1:]):
      highest_zs = int(ans[1:])
    
  

start_n = len(variables)

while len(variables) < start_n + len(statements):

  for x1, op, x2, _, ans in statements:
    
    if x1 in variables and x2 in variables:
      val1 = variables[x1]
      val2 = variables[x2]

      if op == "AND":
        variables[ans] = val1 & val2 
      elif op == "OR":
        variables[ans] = val1 | val2
      elif op == "XOR":
        variables[ans] = val1 ^ val2 
      else:
        raise Exception(f"Operator {op} is not valid")
      

res = 0

for i in range(highest_zs + 1):
  if i < 10:
    z = "z0" + str(i)
  else:
    z = "z" + str(i)
  
  if variables[z] == 1:
    res += 1 << i
  
print(res)
  