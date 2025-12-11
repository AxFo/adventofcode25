import sys
import numpy as np
import math
import matplotlib.pyplot as plt

input_file = "input/9.ex" if len(sys.argv) < 2 else sys.argv[1]

with open(input_file, "r") as f:
    lines = f.readlines()
    lines = [ l.strip() for l in lines ]

tiles = []
for line in lines:
    cs, rs = [ int(v) for v in line.split(",") ]
    tiles.append((rs, cs))

fig, ax = plt.subplots(figsize=(10,10))
for i, tile in enumerate(tiles):
    next = tiles[(i+1)%len(tiles)]
    plt.plot([tile[0], next[0]], [tile[1], next[1]], "--")

ax.axis('equal')
plt.show()
