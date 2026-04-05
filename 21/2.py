# Seriously, the only difference was to change NUM_OF_DIRPADS from 3 to 26


from functools import lru_cache
from collections import deque

with open("input.txt","r") as f:
  codes = [list(row.strip()) for row in f.readlines()]


numpad = [["7","8","9"],
          ["4","5","6"],
          ["1","2","3"],
          [None,"0","A"]]

dirpad = [[None,"^","A"],
          ["<","v",">"]]


def bfs_all(pad):
    WIDTH, HEIGHT = len(pad[0]), len(pad)
    flatten_pad = [x for row in pad for x in row]
    dic = {}
    for i, start in enumerate(flatten_pad):
        if not start: continue
        start_to_end = {}
        queue = deque()
        queue.append((i, ""))
        best = {}
        while queue:
            index, steps = queue.popleft()
            if index in best and len(best[index]) < len(steps): continue
            best[index] = steps
            row, col = index // WIDTH, index % WIDTH
            key = pad[row][col]
            if key:
                start_to_end.setdefault(key, []).append(steps)
            for rowi, coli, d in [(row,col+1,">"),
                                  (row-1,col,"^"),
                                  (row,col-1,"<"),
                                  (row+1,col,"v")]:
                if 0 <= rowi < HEIGHT and 0 <= coli < WIDTH and pad[rowi][coli]:
                    ni = rowi * WIDTH + coli
                    new_steps = steps + d
                    if ni not in best or len(best[ni]) >= len(new_steps):
                        queue.append((ni, new_steps))
        dic[start] = start_to_end
    return dic




NUM_OF_DIRPADS = 26

dir_keypad = bfs_all(dirpad)
num_keypad = bfs_all(numpad)

@lru_cache(maxsize=None)
def min_cost(seq, depth):
    if depth == 0:
        return len(seq)
    total = 0
    pos = "A"
    for ch in seq:
        paths = dir_keypad[pos][ch]
        total += min(min_cost(p + "A", depth - 1) for p in paths)
        pos = ch
    return total

total = 0
for code in codes:
    number = int("".join(code[:-1]))
    seq = ""
    pos = "A"
    for ch in code:
        # pick best way already on numpad level
        paths = num_keypad[pos][ch]
        best = min(paths, key=lambda p: min_cost(p + "A", NUM_OF_DIRPADS - 1))
        seq += best + "A"
        pos = ch
    total += number * min_cost(seq, NUM_OF_DIRPADS - 1)

print(total)