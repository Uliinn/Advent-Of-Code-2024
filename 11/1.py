


stones = []
with open("input.txt","r") as f:
  for v in f.readline().split():
    stones.append(int(v))

for i in range(25):
  new_stones = []

  for stone in stones:
    if stone == 0:
      new_stones.append(1)
    elif len(str(stone)) % 2 == 0:
      str_stone = str(stone)
      left = int(str_stone[0:len(str_stone)//2])
      right = int(str_stone[len(str_stone)//2:])

      new_stones.append(left)
      new_stones.append(right)
    else: 
      new_stones.append(2024 * stone)
  
  stones = new_stones


print(len(stones))