

# Just add 10000000000000 to the answer
total = 0
with open("input.txt","r") as f:
  inp = list(filter(lambda x: x != '\n',f.readlines()))
  inp = [v.strip() for v in inp]
  i = 0
  while i + 2 < len(inp):
    buttonA = inp[i]
    buttonB = inp[i+1]
    prize   = inp[i+2]

    _, ax, ay  = buttonA.split("+")
    ax = ax.split(",")[0]
    _, bx, by  = buttonB.split("+")
    bx = bx.split(",")[0]

    _, px, py = prize.split("=")
    px = px.split(",")[0]

    ax, ay = int(ax), int(ay)
    bx, by = int(bx), int(by)
    px, py = int(px)+10000000000000, int(py)+10000000000000

    det = (ax*by - bx*ay)
    if det == 0:
      i += 3
      continue # not possible

    a = (by*px - bx*py) / det
    b = (-ay*px + ax*py) / det
    
    if a.is_integer() and b.is_integer():
      total += 3*int(a) + int(b)
    
    i += 3
print(total)
    

