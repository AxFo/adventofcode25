import sys

input_file = "input/1.ex" if len(sys.argv) < 2 else sys.argv[1]

with open(input_file, "r") as f:
    lines = f.readlines()
    lines = [ l.strip() for l in lines ]

part_a = False
position = 50
counter = 0
for l in lines:
    sign = 1 if l[0] == 'R' else -1
    value = int(l[1:])
    if part_a:
        modification = sign * value
        position = (position + modification) % 100
        if position == 0:
            counter += 1
    else:
        modification = sign
        for _ in range(value):
            position = (position + modification) % 100

            if position == 0:
                counter += 1

print(counter)
