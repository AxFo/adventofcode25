import sys
import numpy as np
import math

input_file = "input/8.ex" if len(sys.argv) < 2 else sys.argv[1]

with open(input_file, "r") as f:
    lines = f.readlines()
    lines = [ l.strip() for l in lines ]

class Box:
    
    def __init__(self, id, coords):
        self.id = id
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]
        self.circuit = None

    def __repr__(self):
        return f"{self.id} ({self.x}, {self.y}, {self.z}) {self.circuit}"

    def set_circuit(self, circuit):
        self.circuit = circuit

    def distance(self, box):
        dx = self.x - box.x
        dy = self.y - box.y
        dz = self.z - box.z
        return math.sqrt(dx*dx + dy*dy + dz*dz)

class Circuit:

    def __init__(self, id, box):
        self.id = id
        self.boxes = { box }
        box.set_circuit(self)

    def __repr__(self):
        return f"{{{self.id}={len(self)}}}"

    def __len__(self):
        return len(self.boxes)

    def __gt__(self, other):
        return len(self) > len(other)

    def merge(self, circuit):
        for box in circuit.boxes:
            self.boxes.add(box)
            box.set_circuit(self)

boxes = [ Box(i, [ int(t) for t in line.split(",") ]) for i, line in enumerate(lines) ]

# D = [ [ -1 ] * len(boxes) for _ in range(len(boxes)) ]
# for i, box in enumerate(boxes):
#    for j in range(i+1, len(boxes)):
#        D[i][j] = box.distance(boxes[j])

D = []
for i, box in enumerate(boxes):
    for j in range(i+1, len(boxes)):
        D.append((box.distance(boxes[j]), box, boxes[j]))

D = sorted(D)

circuits = [ Circuit(i, box) for i, box in enumerate(boxes) ]

num_steps = 1000 # 10 for 8.ex, 1000 for 8.in
num_largest = 3
b1 = None
b2 = None
#for _ in range(num_steps): # Part A
while len(circuits) > 1: # Part B
    d, b1, b2 = D.pop(0)
    c1 = b1.circuit
    c2 = b2.circuit
    if c1 == c2:
        continue
    c1.merge(c2)
    circuits.remove(c2)

circuits = sorted(circuits)
print(circuits)

part_a = 1
for c in circuits[-num_largest:]:
    part_a *= len(c)

print("Part A", part_a)
print("Part B", b1.x * b2.x)
