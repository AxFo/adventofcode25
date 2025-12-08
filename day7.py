import sys
import numpy as np

input_file = "input/7.ex" if len(sys.argv) < 2 else sys.argv[1]

with open(input_file, "r") as f:
    lines = f.readlines()
    lines = [ l.strip() for l in lines ]

size = len(lines[0])

power = [0] * size
part_a = 0
for line in lines:
    for i, c in enumerate(line):
        if c == "S":
            power[i] += 1
        elif c == "^" and power[i] > 0:
            if i > 0:
                power[i-1] += 1
            if i < size-1:
                power[i+1] += 1
            power[i] = 0
            part_a += 1

print(part_a)
