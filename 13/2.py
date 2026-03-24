

# Just add 10000000000000 to the answer
from z3 import Ints, Solver, sat

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
    px, py = int(px), int(py)

    solver = Solver()
    a,b = Ints("a b")

    solver.add(a * ax + b * bx == px + 10000000000000)
    solver.add(a * ay + b * by == py + 10000000000000)

    if solver.check() == sat:
      answer = solver.model()
      total += 3* answer[a].as_long() + answer[b].as_long()
    
    i += 3
print(total)
    

