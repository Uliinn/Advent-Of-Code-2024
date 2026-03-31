"""Advent of Code[About][Events][Shop][Settings][Log Out]Uliinn 31*
  {:year 2024}[Calendar][AoC++][Sponsors][Leaderboards][Stats]
Our sponsors help make Advent of Code possible:
Zero To Mastery - Ready to upgrade your earning power? If you like AoC, you'll like our courses built by programmers (not influencers), for programmers. ZTM helps you get a better job, and earn more with one trick: quality, not gimmicks.
--- Day 16: Reindeer Maze ---
It's time again for the Reindeer Olympics! This year, the big event is the Reindeer Maze, where the Reindeer compete for the lowest score.

You and The Historians arrive to search for the Chief right as the event is about to start. It wouldn't hurt to watch a little, right?

The Reindeer start on the Start Tile (marked S) facing East and need to reach the End Tile (marked E). They can move forward one tile at a time (increasing their score by 1 point), but never into a wall (#). They can also rotate clockwise or counterclockwise 90 degrees at a time (increasing their score by 1000 points).

To figure out the best place to sit, you start by grabbing a map (your puzzle input) from a nearby kiosk. For example:

###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
There are many paths through this maze, but taking any of the best paths would incur a score of only 7036. This can be achieved by taking a total of 36 steps forward and turning 90 degrees a total of 7 times:


###############
#.......#....E#
#.#.###.#.###^#
#.....#.#...#^#
#.###.#####.#^#
#.#.#.......#^#
#.#.#####.###^#
#..>>>>>>>>v#^#
###^#.#####v#^#
#>>^#.....#v#^#
#^#.#.###.#v#^#
#^....#...#v#^#
#^###.#.#.#v#^#
#S..#.....#>>^#
###############
Here's a second example:

#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
In this maze, the best paths cost 11048 points; following one such path would look like this:

#################
#...#...#...#..E#
#.#.#.#.#.#.#.#^#
#.#.#.#...#...#^#
#.#.#.#.###.#.#^#
#>>v#.#.#.....#^#
#^#v#.#.#.#####^#
#^#v..#.#.#>>>>^#
#^#v#####.#^###.#
#^#v#..>>>>^#...#
#^#v###^#####.###
#^#v#>>^#.....#.#
#^#v#^#####.###.#
#^#v#^........#.#
#^#v#^#########.#
#S#>>^..........#
#################
Note that the path shown above includes one 90 degree turn as the very first move, rotating the Reindeer from facing East to facing North.

Analyze your map carefully. What is the lowest score a Reindeer could possibly get?

To begin, get your puzzle input.

Answer: 
 

You can also [Share] this puzzle."""


import heapq
start = None
with open("input.txt","r") as f:
  inp = f.readlines()

  grid = [list(row.strip()) for row in inp]

  for y in range(len(grid)):
    for x in range(len(grid[y])):
      if grid[y][x] == "S":
        
        start = (x,y)

EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


WIDTH = len(grid[0])
HEIGHT = len(grid)

heap = [(0,start,EAST)] # cost, (x,y), direction
visited = set()
while heap:
  cost, (x,y), direction= heapq.heappop(heap)

  if grid[y][x] == "E":
    print(cost)
    break

  visited.add((x,y))

  for xi,yi,di in [(x+1,y,EAST), (x,y-1,NORTH),(x-1,y,WEST),(x,y+1,SOUTH)]: #east, north, west, south

    if 0 <= xi < WIDTH and 0 <= yi < HEIGHT and (xi,yi) not in visited:
      
      if grid[yi][xi] == "#": # a wall
        continue
      d = abs(di - direction)
      if d == 3: d = 1
      costi = cost + 1 + 1000 * d
      heapq.heappush(heap,(costi,(xi,yi),di)) 


