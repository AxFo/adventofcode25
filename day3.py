import sys

input_file = "input/3.ex" if len(sys.argv) < 2 else sys.argv[1]

with open(input_file, "r") as f:
    lines = f.readlines()
    lines = [ l.strip() for l in lines ]

result = 0
for line in lines:
    first = 0
    second = 0
    for i, d in enumerate(line):
        n = int(d)
        if i < len(line)-1 and n > first:
            first = n
            second = 0
        elif n > second:
            second = n
    joltage = first * 10 + second
    print(joltage)
    result += joltage

print("Result:", result)
