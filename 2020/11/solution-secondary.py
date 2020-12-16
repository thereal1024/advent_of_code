#!/usr/bin/env python3

DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def coord_is_valid(state, x, y):
    return y in range(len(state)) and x in range(len(state[0]))

def unchk_get_occupied_coord(state, x, y):
    return state[y][x] == '#'

def unchk_get_is_floor_coord(state, x, y):
    return state[y][x] == '.'

def occ_in_dir(state, x, y, direc, mr):
    for i in mr:
        cx, cy = x + direc[0] * i, y + direc[1] * i
        if not coord_is_valid(state, cx, cy):
            return False
        if unchk_get_is_floor_coord(state, cx, cy):
            continue
        return unchk_get_occupied_coord(state, cx, cy)
    raise Exception('should have enumerated enough coords')

def state_next(state, x, y):
    cstate = state[y][x]
    if cstate == '.':
        return cstate
    mr = range(1, max(len(state), len(state[0])))
    adj_occ = sum(occ_in_dir(state, x, y, direc, mr) for direc in DIRS)

    if cstate == 'L':
        return '#' if adj_occ == 0 else cstate
    elif cstate == '#':
        return 'L' if adj_occ >= 5 else cstate
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
