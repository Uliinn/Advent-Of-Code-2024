from collections import defaultdict
with open("input.txt","r") as f:
  inp = [v.strip().split("-") for v in f.readlines()]

ts = set()
paths = defaultdict(list)
for v1,v2 in inp: # dict for path, both ways, #if t in name, add to a set
  paths[v1].append(v2)
  paths[v2].append(v1)
  if v1[0] == "t":
    ts.add(v1)
  if v2[0] == "t":
    ts.add(v2)


# DFS on all nodes with a t, and stop adding to stack when steps == 3,
# everytime the same node starting with t comes up with the steps of 3, add to triangle set
triangles_including_t = set()
for t in ts:
  stack = [(0,t,())]

  while stack:

    steps, node, parents = stack.pop()
    
    next_nodes = paths[node]
    parents = (node, *parents)
    for new_node in next_nodes:
      if len(parents) == 3:
        if new_node == t:
          parents = sorted(list(parents))
          triangles_including_t.add(tuple(parents))
        continue 

      stack.append((steps+1,new_node, parents))

print(len(triangles_including_t))

