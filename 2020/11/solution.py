#!/usr/bin/env python3

def get_occupied_coord(state, x, y):
    if y not in range(len(state)) or x not in range(len(state[0])):
        return False
    return state[y][x] == '#'

def state_next(state, x, y):
    cstate = state[y][x]
    if cstate == '.':
        return cstate
    adj_occ = 0
    for cy in range(y-1, y+2):
        for cx in range(x-1, x+2):
            if (cx, cy) != (x, y) and get_occupied_coord(state, cx, cy):
                adj_occ += 1
    if cstate == 'L':
        return '#' if adj_occ == 0 else cstate
    elif cstate == '#':
        return 'L' if adj_occ >= 4 else cstate
    else:
        raise Exception('unknown state: ' + cstate)

def evolution_step(state):
    height = len(state)
    width = len(state[0])
    return [''.join(state_next(state, x, y) for x in range(width)) for y in range(height)]

def count_seated(state):
    return sum(row.count('#') for row in state)

def solution(lines):
    state = list(lines)
    width = len(state[0])
    assert all(len(row) == width for row in state)

    while True:
        next_state = evolution_step(state)
        if next_state == state:
            break
        state = next_state
    
    final_seated = count_seated(state)
    print(f"Solution: {final_seated}")

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
