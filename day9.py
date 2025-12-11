import sys
import numpy as np
import math

input_file = "input/9.ex" if len(sys.argv) < 2 else sys.argv[1]

with open(input_file, "r") as f:
    lines = f.readlines()
    lines = [ l.strip() for l in lines ]

tiles = []
x_max = 0
y_max = 0
for line in lines:
    xs, ys = line.split(",")
    xs = int(xs)
    ys = int(ys)
    if xs > x_max:
        x_max = xs
    if ys > y_max:
        y_max = ys
    tiles.append((xs, ys))

max_size = 0
for a in tiles:
    for b in tiles:
        if a[0] > b[0]:
            continue
        dx = abs(a[0] - b[0])
        dy = abs(a[1] - b[1])
        size = (dx+1) * (dy+1)
        if size > max_size:
            max_size = size

print("Part A", max_size)

def print_grid(G):
    for line in G:
        print("".join(line.astype(str)))

def corner_type(prev, tile, next):
    """
    Returns / for upper-left and lower-right corners, \\ otherwise.
    """
    min_0 = min(prev[0], tile[0], next[0])
    max_0 = max(prev[0], tile[0], next[0])
    min_1 = min(prev[1], tile[1], next[1])
    max_1 = max(prev[1], tile[1], next[1])
    if tile[0] == min_0 and tile[1] == min_1:
        return b'/'
    if tile[0] == min_0 and tile[1] == max_1:
        return b'\\'
    if tile[0] == max_0 and tile[1] == min_1:
        return b'\\'
    if tile[0] == max_0 and tile[1] == max_1:
        return b'/'
    assert False

def line_type(tile, next):
    """
    Returns whether the line from tile to next is horizontal or vertical.
    """
    if tile[0] == next[0]:
        return "vertical"
    if tile[1] == next[1]:
        return "horizontal"
    assert False

def is_inner(c, r, G):
    """
    Returns True if the cell G[c][r] in the grid is inside the loop
    """
    if G[c][r] == b'.':
        return True

    if G[c][r] == b'o':
        return False

    if G[c][r] != b'?':
        return False

    count = 0
    for col in range(c):
        if G[col][r] == b'/':
            count += 0.5
        elif G[col][r] == b'\\':
            count -= 0.5
        elif G[col][r] == b'-':
            count += 1
    return count % 2 != 0

def valid_rectangle(a, b, G):
    min_0 = min(a[0], b[0])
    max_0 = max(a[0], b[0])
    min_1 = min(a[1], b[1])
    max_1 = max(a[1], b[1])

    if np.all(G[min_1:max_1, min_0:max_0] != b'o'):
        return (max_0 - min_0 + 1) * (max_1 - min_1 + 1)
    return 0

def rectangle_size(a, b, G):
    min_0 = min(a[0], b[0])
    max_0 = max(a[0], b[0])
    min_1 = min(a[1], b[1])
    max_1 = max(a[1], b[1])

    return (max_0 - min_0 + 1) * (max_1 - min_1 + 1)

# create grid and outline
print("outline")
n_rows = x_max + 2
n_cols = y_max + 2
G = np.full((n_cols, n_rows), b'?', dtype='S1')
for i, tile in enumerate(tiles):
    prev = tiles[(i-1)%len(tiles)]
    next = tiles[(i+1)%len(tiles)]
    G[tile[1], tile[0]] = corner_type(prev, tile, next)
    if line_type(tile, next) == "horizontal":
        c1 = tile[1]
        G[c1, min(tile[0], next[0])+1:max(tile[0], next[0])] = b'-'
    else:
        c0 = tile[0]
        G[min(tile[1], next[1])+1:max(tile[1], next[1]), c0] = b'|'
    print(f"tile {i}/{len(tiles)} done")

part_b = 0
for i, a in enumerate(tiles):
    for b in tiles:
        if a[0] > b[0]:
            continue
        size = rectangle_size(a, b, G)
        if size <= part_b:
            continue
        min_0 = min(a[0], b[0])
        max_0 = max(a[0], b[0])
        min_1 = min(a[1], b[1])
        max_1 = max(a[1], b[1])

        valid = True
        for c0 in range(min_0, max_0+1):
            for c1 in range(min_1, max_1+1):
                if G[c1][c0] == b'o':
                    valid = False
                    break
                elif G[c1][c0] == b'.' or G[c1][c0] != b'?':
                    pass
                elif is_inner(c1, c0, G):
                    #print("is inner", c1, c0)
                    G[c1, c0] = b'.'
                else:
                    #print("is outer", c1, c0)
                    G[c1, c0] = b'o'
                    valid = False
            if not valid:
                break
        if not valid:
            continue

        part_b = size
        print(a, b, size)
    print(f"tile {i}/{len(tiles)} done")

if x_max < 30:
    print_grid(G)

print("Part B", part_b)
