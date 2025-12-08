import sys
import numpy as np

input_file = "input/7.ex" if len(sys.argv) < 2 else sys.argv[1]

with open(input_file, "r") as f:
    lines = f.readlines()
    lines = [ l.strip() for l in lines ]

size = len(lines[0])

power = [0] * size
part_a = 0
part_b = 0

for line in lines:
    for i, c in enumerate(line):
        if c == "S":
            power[i] = 1
            break
        elif c == "^" and power[i] > 0:
            if i > 0:
                power[i-1] += power[i]
            if i < size-1:
                power[i+1] += power[i]
            power[i] = 0
            part_a += 1
    print(power)

part_b = sum(power)
print("Part A", part_a)
print("Part B", part_b)
