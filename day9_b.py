import sys
import numpy as np
import math
import matplotlib.pyplot as plt

input_file = "input/9.ex" if len(sys.argv) < 2 else sys.argv[1]

with open(input_file, "r") as f:
    lines = f.readlines()
    lines = [ l.strip() for l in lines ]

tiles = []
r_max = 0
c_max = 0
for line in lines:
    cs, rs = [ int(v) for v in line.split(",") ]
    if rs > r_max:
        r_max = rs
    if cs > c_max:
        c_max = cs
    tiles.append((rs, cs))

num_rows = r_max + 2
num_cols = c_max + 2

C = set([0])
for v in set([t[1] for t in tiles]):
    C.add(v)
    C.add(v+1)
C = sorted(list(C))
nc = len(C)

R = set([0])
for v in set([t[0] for t in tiles]):
    R.add(v)
    R.add(v+1)
R = sorted(list(R))
nr = len(R)


def print_grid(G, nr=500, nc=500):
    for l in G[:nr]:
        print("".join(l)[:nc])

def corner_type(prev, tile, next):
    """
    Returns / for upper-left and lower-right corners, \\ otherwise.
    """
    min_r = min(prev[0], tile[0], next[0])
    max_r = max(prev[0], tile[0], next[0])
    min_c = min(prev[1], tile[1], next[1])
    max_c = max(prev[1], tile[1], next[1])
    if tile[0] == min_r and tile[1] == min_c:
        return '/'
    if tile[0] == min_r and tile[1] == max_c:
        return '\\'
    if tile[0] == max_r and tile[1] == min_c:
        return '\\'
    if tile[0] == max_r and tile[1] == max_c:
        return '/'
    assert False

def line_type(tile, next):
    """
    Returns whether the line from tile to next is horizontal or vertical.
    """
    if tile[1] == next[1]:
        return "vertical"
    if tile[0] == next[0]:
        return "horizontal"
    assert False

def is_inner(r, c, G):
    """
    Returns True if the cell G[c][r] in the grid is inside the loop
    """
    if G[r][c] == '.':
        return True

    if G[r][c] == 'o':
        return False

    if G[r][c] != '?':
        return False

    count = 0
    for row in range(r):
        if G[row][c] == '/':
            count += 0.5
        elif G[row][c] == '\\':
            count -= 0.5
        elif G[row][c] == '-':
            count += 1
    return count % 2 != 0

def rectangle_size(a, b):
    min_0 = min(a[0], b[0])
    max_0 = max(a[0], b[0])
    min_1 = min(a[1], b[1])
    max_1 = max(a[1], b[1])

    return (max_0 - min_0 + 1) * (max_1 - min_1 + 1)

G = [ ['?'] * nc for _ in range(nr) ]
#fig, ax = plt.subplots(figsize=(10,10))
for i, tile in enumerate(tiles):
    prev = tiles[(i-1) % len(tiles)]
    next = tiles[(i+1) % len(tiles)]
    pr = R.index(prev[0])
    pc = C.index(prev[1])
    sr = R.index(tile[0])
    sc = C.index(tile[1])
    er = R.index(next[0])
    ec = C.index(next[1])

    #plt.plot([sr, er], [sc, ec], "--")
    corner = corner_type(prev, tile, next)
    G[sr][sc] = corner
    
    sc, ec = sorted([sc, ec])
    sr, er = sorted([sr, er])
    if sc == ec:
        for r in range(sr+1, er):
            G[r][sc] = '|'
    elif sr == er:
        for c in range(sc+1, ec):
            G[sr][c] = '-'
    else:
        assert False

#plt.show()

for r in range(nr):
    for c in range(nc):
        if G[r][c] == '?':
            if is_inner(r, c, G):
                G[r][c] = '#'
            else:
                G[r][c] = '.'

#print(R)
#print(C)
#print_grid(G, 20, 80)
print_grid(G)

part_b = 0
for a in tiles:
    for b in tiles:
        if a[0] > b[0]:
            continue

        size = rectangle_size(a, b)
        if size <= part_b:
            continue

        ra = R.index(a[0])
        rb = R.index(b[0])
        ca = C.index(a[1])
        cb = C.index(b[1])
        ra, rb = sorted([ra, rb])
        ca, cb = sorted([ca, cb])

        valid = True
        for r in range(ra, rb+1):
            for c in range(ca, cb+1):
                if G[r][c] == '.':
                    valid = False
                    break
            if not valid:
                break

        if valid:
            part_b = size

print("Part B", part_b)
