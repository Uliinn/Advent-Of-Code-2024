

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

at_least_100 = 0
for x,y in all_free_spaces:

  time = seconds_array[y][x]

  cheat_length = 20

  for dx in range(-cheat_length, cheat_length + 1):
      for dy in range(-(cheat_length - abs(dx)), (cheat_length - abs(dx)) + 1):
          dist = abs(dx) + abs(dy)
          if dist < 2: # Cant be less than 2 steps
              continue
          xi, yi = x + dx, y + dy
          if not ((0 <= xi < WIDTH) and (0 <= yi < HEIGHT)):
              continue
          new_time = seconds_array[yi][xi]
          if new_time == WALL:
              continue
          if time - (new_time + dist) >= 100:
              at_least_100 += 1

print(at_least_100)