
with open("input.txt","r") as f:
  inp = [row.strip() for row in f.readlines()]
  
  height,width  = len(inp), len(inp[0])
  
  freq_map = {}
  freqs = set()

  for y,row in enumerate(inp):
    for x,symbol in enumerate(list(row)):

      if symbol != ".":
        if symbol in freqs:
          freq_map[symbol].append((y,x))
        else:
          freqs.add(symbol)
          freq_map[symbol] = [(y,x)]
  
  antinodes = set()

  for symbol in freqs:

    positions = freq_map[symbol]

    for i in range(len(positions)):
      pos1 = positions[i]
      for j in range(i+1,len(positions)):
        pos2 = positions[j]

        vec = (pos2[0]-pos1[0], pos2[1]-pos1[1]) # Vector from pos1 to pos2

        # 2 possible antinodes per pair of points
        # one at pos1 + 2 * vec, and one at pos1 - vec

        antinode1 = (pos1[0] + 2 * vec[0], pos1[1] + 2 * vec[1])

        if 0 <= antinode1[0] < height and 0 <= antinode1[1] < width:
          if antinode1 not in antinodes:
            antinodes.add(antinode1)

        antinode2 = (pos1[0] - vec[0], pos1[1] - vec[1])

        if 0 <= antinode2[0] < height and 0 <= antinode2[1] < width:
          if antinode2 not in antinodes:
            antinodes.add(antinode2)
        

  print(len(antinodes))
