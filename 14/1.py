
# Robots can be at same place in a given time
# Just calculate how many steps in x and y directons the robot has taken after 100 seconds
# Add that to the starting position and use modulo <dimension>
# For each robot, check in which quadrant they are in, or if they are in the middle of any
WIDTH = 101
HEIGHT = 103  
quadrants = [0, # upper left
             0, # upper right
             0, # down left
             0] # down right
with open("input.txt","r") as f:
  
  for row in f.readlines():
    left, right = row.strip().split()

    x,y = map(int,left.split("=")[1].split(","))
    
    vx, vy = map(int,right.split("=")[1].split(","))

    x = (x + 100*vx) % WIDTH
    y = (y + 100*vy) % HEIGHT 

    if x == WIDTH // 2 or y == HEIGHT // 2:
      continue # In between some quadrants

    left_side = False
    up = False
    if x < WIDTH // 2: # Left:
       left_side = True
    if y < HEIGHT // 2:
      up = True
    
    if left_side and up:
      quadrants[0] += 1
    elif not left_side and up:
      quadrants[1] += 1
    elif left_side and not up:
      quadrants[2] += 1
    elif not left_side and not up:
      quadrants[3] += 1
    else:
      raise Exception("What?")

product = 1

for robots in quadrants:
  product *= robots

print(product)