import sys
import numpy as np
import scipy.linalg
import math

input_file = "input/10.ex" if len(sys.argv) < 2 else sys.argv[1]

with open(input_file, "r") as f:
    lines = f.readlines()
    lines = [ l.strip() for l in lines ]

part_b = 0
for line in lines:
    token, rest = line.split("]")
    requirement = token[1:]

    token, rest = rest.split("{")
    buttons = [ tuple( int(x) for x in t[:-2].split(",") ) for t in token.split("(")[1:] ]

    num_output = len(requirement)
    num_buttons = len(buttons)

    joltage = [ int(j) for j in rest[:-1].split(",") ]
    
    A = np.zeros((num_output, num_buttons))
    b = np.zeros((num_output, 1))
    for i in range(num_output):
        b[i] = joltage[i]

    for k, button in enumerate(buttons):
        for i in button:
            A[i, k] = 1

    L, U = scipy.linalg.lu(A, permute_l=True)
    print(L)
    print(U)
    x = np.linalg.pinv(A) @ b
    x_int = np.rint(x).astype(int)

    print("A", A)
    print("b", np.transpose(b))
    print("x", np.transpose(x))
    print("sum", np.sum(x_int))
    break
