# Recursion until only one is found then return

def recursive_check_possible(goal,current_sum,nums,nums_idx) -> bool:

  if nums_idx == len(nums): return goal == current_sum

  # add
  if recursive_check_possible(goal,current_sum+nums[nums_idx],nums,nums_idx+1):
    return True

  # multiply
  if recursive_check_possible(goal,current_sum*nums[nums_idx],nums,nums_idx+1):
    return True
  
  return False


with open("input.txt","r") as f:
  inp = [row.strip() for row in f.readlines()]

  equations = []
  for i in range(len(inp)):
    goal, nums = inp[i].split(":")
    nums = [int(v) for v in nums.strip().split()]
    equations.append((int(goal),nums))

  total = 0
  for goal, nums in equations:
    if recursive_check_possible(goal,nums[0],nums,1): # nums_idx = 1 because we already added nums[0]
      total += goal
  
  print(total)
  



