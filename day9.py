import sys
import numpy as np
import math

input_file = "input/9.ex" if len(sys.argv) < 2 else sys.argv[1]

with open(input_file, "r") as f:
    lines = f.readlines()
    lines = [ l.strip() for l in lines ]

tiles = []
for line in lines:
    xs, ys = line.split(",")
    tiles.append((int(xs), int(ys)))

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
