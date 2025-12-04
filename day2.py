import sys

input_file = "input/2.ex" if len(sys.argv) < 2 else sys.argv[1]

with open(input_file, "r") as f:
    lines = f.readlines()
    lines = [ l.strip() for l in lines ]

ranges = lines[0].split(",")

part_a = True
result = 0
for r in ranges:
    tokens = r.split("-")
    start = int(tokens[0])
    end = int(tokens[1])
    for i in range(start, end+1):
        string = str(i)
        n = len(string)
        for d in range(2,n+1):
            if n % d != 0:
                if part_a:
                    break
                continue
            chunk_size = int(n/d)
            chunks = [ string[j:j+chunk_size] for j in range (0, n, chunk_size) ]
            if chunks.count(chunks[0]) == len(chunks):
                print(string)
                result += i
                break
            if part_a:
                break

print("Result:", result)
