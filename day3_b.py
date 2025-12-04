import sys

input_file = "input/3.ex" if len(sys.argv) < 2 else sys.argv[1]

with open(input_file, "r") as f:
    lines = f.readlines()
    lines = [ l.strip() for l in lines ]

result = 0
num_batteries = 12
for line in lines:
    active = [0] * num_batteries
    active_index = [-1] * (num_batteries + 1)
    for battery in range(num_batteries-1,-1,-1):
        for i in range(active_index[battery]+1,len(line)-battery):
            d = line[i]
            n = int(d)
            if n > active[battery]:
                active[battery] = n
                active_index[battery-1] = i
    joltage = 0
    for i in range(num_batteries):
        joltage += active[i] * 10 ** i

    print(list(reversed(active)), joltage)
    result += joltage

print(result)
        
