import sys
import numpy as np
import math

input_file = "input/10.ex" if len(sys.argv) < 2 else sys.argv[1]

with open(input_file, "r") as f:
    lines = f.readlines()
    lines = [ l.strip() for l in lines ]

def to_string(state):
    return ",".join([ str(v) for v in state ])

def press_button(state, button):
    valid = True
    new_state = list(state)
    for v in button:
        new_state[v] -= 1
        if new_state[v] < 0:
            valid = False
            break

    return new_state if valid else None

part_b = 0
for line in lines:
    _, rest = line.split("]")

    token, rest = rest.split("{")
    buttons = [ tuple( int(x) for x in t[:-2].split(",") ) for t in token.split("(")[1:] ]

    joltage = [ int(j) for j in rest[:-1].split(",") ]
    num_joltages = len(joltage)

    test = [0] * num_joltages
    for b in buttons:
        for s in b:
            test[s] += 1
    print(test)
    continue
    print(buttons, joltage)

    states = { to_string(joltage): None }
    final_state = [0] * num_joltages
    Q = [ joltage ]
    found = False
    while len(Q) > 0:
        state = Q.pop(0)
        print(state)
        for b, button in enumerate(buttons):
            next_state = press_button(state, button)
            if next_state:
                as_string = to_string(next_state)
                if not as_string in states:
                    states[as_string] = (b, state)
                    Q.append(next_state)
                    #print("  ", button, next_state)

                if next_state == final_state:
                    print("FOUND")
                    found = True
                    break
        if found:
            break
    
    print("Backtracking")
    state = final_state
    button_presses = []
    while state != joltage:
       b, prev = states[to_string(state)] 
       button_presses.append(b)
       #print(b, prev)
       state = prev

    print(button_presses)
    part_b += len(button_presses)

print("Part B", part_b)
