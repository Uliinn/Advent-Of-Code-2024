import numpy as np

WALL = -1
with open("input.txt","r") as f:
  inp = f.readlines()
  grid = [list(row.strip()) for row in inp]


seconds_array = []
start = None

end = None
all_free_spaces = []
for y,row in enumerate(grid):
  seconds_row = []
  for x,symbol in enumerate(row):
    if symbol == "#":
      seconds_row.append(WALL)
    else:
      all_free_spaces.append((x,y))
      seconds_row.append(0)
    if symbol == "S":
      start = (x,y)
    elif symbol == "E":
      end = (x,y)
  seconds_array.append(seconds_row)



pos = end
time = 0
while pos != start:
  seconds_array[pos[1]][pos[0]] = time
  time += 1
  for xi,yi in [(pos[0]+1,pos[1]), (pos[0],pos[1]-1), (pos[0]-1,pos[1]), (pos[0],pos[1]+1)]: # R U L D
    if (grid[yi][xi] == "." or grid[yi][xi] == "S") and seconds_array[yi][xi] == 0:
      pos = (xi,yi)
      break

seconds_array[start[1]][start[0]] = time # Last step that doesnt get covered by the previous while loop

WIDTH = len(grid[0])
HEIGHT = len(grid)



sa = np.array(seconds_array)  # konvertera en gång innan loopen

at_least_100 = 0
cheat_length = 20

for x, y in all_free_spaces:
    t = sa[y, x]
    if t == 0 and (x, y) != end:
        continue

    # Cut out a window around (x,y)
    x0, x1 = max(0, x - cheat_length), min(WIDTH, x + cheat_length + 1)
    y0, y1 = max(0, y - cheat_length), min(HEIGHT, y + cheat_length + 1)

    window = sa[y0:y1, x0:x1]

    # Manhattan-distance for every cell in the window
    ys, xs = np.ogrid[y0-y:y1-y, x0-x:x1-x]
    dist = np.abs(xs) + np.abs(ys)

    mask = (dist >= 2) & (dist <= cheat_length) & (window != WALL)
    savings = t - (window + dist)
    at_least_100 += np.sum((savings >= 100) & mask)

print(at_least_100)