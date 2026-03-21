



#order isn't needed

from collections import defaultdict
stones = defaultdict(int) # stone int: num_of int

cache = {
  0:1
  } # caches the next

with open("input.txt","r") as f:
  for v in f.readline().split():
    stones[int(v)] = 1 


for i in range(75):

  new_stones = defaultdict(int)
  for stone,num in stones.items():
    if stone in cache:

      next_stone = cache[stone]

      if isinstance(next_stone, tuple):
        left, right = next_stone
        new_stones[left] += num 
        new_stones[right] += num
      else:
        new_stones[next_stone] += num

    else:
      if len(str(stone)) % 2 == 0:
        str_stone = str(stone)
        left = int(str_stone[0:len(str_stone)//2])
        right = int(str_stone[len(str_stone)//2:])
        
        cache[stone] = (left,right)
        new_stones[left] += num 
        new_stones[right] += num
      else:
        new_stones[stone * 2024] += num
        cache[stone] = stone * 2024
  stones = new_stones



total = 0

for key in stones:
  total += stones[key]
print(total)