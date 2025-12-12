import sys
import numpy as np
import math

input_file = "input/10.ex" if len(sys.argv) < 2 else sys.argv[1]

with open(input_file, "r") as f:
    lines = f.readlines()
    lines = [ l.strip() for l in lines ]

def press_button(state, button):
    for i in button:
        if state[i] == ".":
            state = state[:i] + '#' + state[i+1:] 
        else:
            state = state[:i] + '.' + state[i+1:]
    return state

def bfs(initial_state, G, final_state):
    Q = [ initial_state ]
    visited = set()
    predecessors = { initial_state: None }

    while len(Q) > 0:
        state = Q.pop(0)
        visited.add(state)
        if state == final_state:
            break

        for button in G[state]:
            neighbor = G[state][button] 
            if not neighbor in visited:
                Q.append(neighbor)
            if not neighbor in predecessors:
                predecessors[neighbor] = (button, state)
                
    button_presses = []
    state = final_state
    while state != initial_state:
        button, predecessor = predecessors[state]
        button_presses.append(button)
        state = predecessor
    
    return button_presses

part_a = 0
for line in lines:
    token, rest = line.split("]")
    requirement = token[1:]

    token, rest = rest.split("{")
    buttons = [ tuple( int(x) for x in t[:-2].split(",") ) for t in token.split("(")[1:] ]

    joltage = [ int(j) for j in rest[:-1].split(",") ]

    print(requirement, buttons, joltage)

    num_bulbs = len(requirement)
    initial_state = "".join(["."] * num_bulbs)
    G = { initial_state: {} }
    queue = []
    queue.append(initial_state)
    while len(queue) > 0:
        state = queue.pop(0)
        for button_index, button in enumerate(buttons):
            next_state = press_button(state, button)
            G[state][button_index] = next_state
            if not next_state in G:
                G[next_state] = {}
                queue.append(next_state)

    button_presses = bfs(initial_state, G, requirement)
    part_a += len(button_presses)
    print(button_presses, " >> ", [ buttons[b] for b in button_presses ])
    #break

print("Part A", part_a)
