# Very weird question
# Apparently check when the variance is the lowest
WIDTH = 101
HEIGHT = 103  

robots = []
with open("input.txt","r") as f:
  
  for row in f.readlines():
    left, right = row.strip().split()

    x,y = map(int,left.split("=")[1].split(","))
    
    vx, vy = map(int,right.split("=")[1].split(","))

    robots.append((x,y,vx,vy))




x_lowest_variance, y_lowest_variance = float("inf"), float("inf")
x_best_t, y_best_t = -1, -1
for t in range(max(WIDTH,HEIGHT)):
  positions = [((x + t*vx) % WIDTH, (y + t*vy) % HEIGHT) 
                 for x, y, vx, vy in robots]
  
  xs = [p[0] for p in positions]
  ys = [p[1] for p in positions]

  x_mean  = sum(xs) / len(xs)
  x_variance = sum([(x - x_mean)**2 for x in xs]) / len(xs)

  y_mean = sum(ys) / len(ys)
  y_variance = sum([(y - y_mean)**2 for y in ys]) / len(ys)


  if x_variance < x_lowest_variance:
    x_lowest_variance = x_variance
    x_best_t = t

  if y_variance < y_lowest_variance:
    y_lowest_variance = y_variance
    y_best_t = t


best_t = x_best_t
# Chinese remainder theroem
while best_t % HEIGHT != y_best_t:
  best_t += WIDTH
print(best_t)
