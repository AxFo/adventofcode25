import sys
import numpy as np

input_file = "input/6.ex" if len(sys.argv) < 2 else sys.argv[1]

with open(input_file, "r") as f:
    lines = f.readlines()
    # lines = [ l.strip() for l in lines ]
    lines = [ l[:-1] for l in lines ]

spaces = set()
for line in lines:
    if len(spaces) == 0:
        for i, c in enumerate(line):
            if c == " ":
                spaces.add(i)
    else:
        to_remove = set()
        for i in spaces:
            if line[i] != " ":
                to_remove.add(i)
        if len(to_remove) > 0:
            spaces = spaces - to_remove

columns = sorted(list(spaces))
print(columns)

num_tasks = len(columns) + 1
print(num_tasks)
tasks = [ [] for _ in range(num_tasks) ]
for line in lines:
    tokens = [ line[i:j].strip() for i,j in zip([0] + columns, columns + [None])]
    try:
        t = [ int(token) for token in tokens ]
        for i in range(num_tasks):
            tasks[i].append(t[i])
    except:
        operands = tokens

print(tasks)

part_a = 0
for i, task in enumerate(tasks):
    if operands[i] == "+":
        result = 0
        for num in task:
            result += num
    elif operands[i] == "*":
        result = 1
        for num in task:
            result *= num
    part_a += result
print(part_a)
