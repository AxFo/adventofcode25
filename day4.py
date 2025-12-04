import sys
import numpy as np

input_file = "input/4.ex" if len(sys.argv) < 2 else sys.argv[1]

with open(input_file, "r") as f:
    lines = f.readlines()
    lines = [ l.strip() for l in lines ]

w = len(lines[0])
h = len(lines)

grid = np.ndarray((w,h))
for r,line in enumerate(lines):
    for c,val in enumerate(line):
        grid[r][c] = 1 if val == '@' else 0

def iterate(grid):
    result = np.ndarray((w,h))
    for r in range(h):
        for c in range(w):
            val = 0
            if (r > 0):
                if (c > 0):
                    val += grid[r-1][c-1]
                if (c < w-1):
                    val += grid[r-1][c+1]
                val += grid[r-1][c]
            if (r < h-1):
                if (c > 0):
                    val += grid[r+1][c-1]
                if (c < w-1):
                    val += grid[r+1][c+1]
                val += grid[r+1][c]
            if (c > 0):
                val += grid[r][c-1]
            if (c < w-1):
                val += grid[r][c+1]
            result[r][c] = val

    result = (result < 4) & (grid == 1) * 1
    num_removed = np.sum(result)
    new_grid = grid
    new_grid[result == 1] = 0
    return num_removed, new_grid

num_removed = -1
removed_first_iteration = -1
total_removed = 0
while num_removed != 0:
    num_removed, grid = iterate(grid)
    if removed_first_iteration == -1:
        removed_first_iteration = num_removed
    total_removed += num_removed
    print("Iteration", num_removed)

print("Part A:", removed_first_iteration)
print("Part B:", total_removed)
