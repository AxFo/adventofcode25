import sys
import numpy as np

input_file = "input/5.ex" if len(sys.argv) < 2 else sys.argv[1]

with open(input_file, "r") as f:
    lines = f.readlines()
    lines = [ l.strip() for l in lines ]

def is_fresh(id, r):
    if id < r[0]:
        return False
    elif id > r[1]:
        return False
    return True

def have_overlap(r1, r2):
    if r1[1] < r2[0] or r2[1] < r1[0]:
        return False
    return True

def merge_ranges(r1, r2):
    return min(r1[0], r2[0]), max(r1[1], r2[1])

ranges = []
ids = []
block1 = True
for line in lines:
    if not line:
        block1 = False
        continue

    if block1:
        tokens = line.split("-")
        start = int(tokens[0])
        end = int(tokens[1])
        ranges.append((start, end))
    else:
        ids.append(int(line))

# merge ranges that overlap
for _ in range(len(ranges)):
    new_ranges = []
    r = ranges[0]
    for i in range(1,len(ranges)):
        if have_overlap(r, ranges[i]):
            r = merge_ranges(r, ranges[i])
        else:
            new_ranges.append(ranges[i])
    new_ranges.append(r)
    ranges = new_ranges

print(ranges)
print(ids)

result = 0
for id in ids:
    for r in ranges:
        if is_fresh(id, r):
            result += 1
            # print(id, "is fresh")
            break

part2 = 0
for r in ranges:
    num_valid = r[1] - r[0] + 1
    print(r, "num valid =", num_valid)
    part2 += num_valid

print("Part One", result)
print("Part Two", part2)

