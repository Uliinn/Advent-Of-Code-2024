
from collections import defaultdict
with open("input.txt","r") as f:
  inp = [v.strip().split("-") for v in f.readlines()]

nodes = set()
paths = defaultdict(list)
node_to_int = {}
int_to_node = {}
i = 0
for v1,v2 in inp: # dict for path, both ways, and nodes
  paths[v1].append(v2)
  paths[v2].append(v1)
  
  if v1 not in nodes:
    node_to_int[v1] = i 
    int_to_node[i] = v1
    i += 1
    nodes.add(v1)
  
  if v2 not in nodes:
    node_to_int[v2] = i 
    int_to_node[i] = v2
    i += 1
    nodes.add(v2)


connected_networks = defaultdict(int) # Maps a bitfield of 520 bits to a frequency
for node in nodes:
  node_paths = paths[node]
  for i in range(2**len(node_paths)):
    neighbours = i 

    bits = 0
    idx = 0
    while neighbours != 0:
      if neighbours & 1 == 1:
        bits += 1 << node_to_int[node_paths[idx]]
      idx += 1
      neighbours = neighbours >> 1
    
    bits += 1 << node_to_int[node]
    connected_networks[bits] += 1

best_network_bits = max(connected_networks,key=connected_networks.get)

largest_network = []
idx = 0
while best_network_bits != 0:
  if best_network_bits & 1 == 1:
    largest_network.append(int_to_node[idx])
  idx += 1
  best_network_bits = best_network_bits >> 1

print(",".join(sorted(largest_network)))