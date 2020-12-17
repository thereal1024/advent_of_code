#!/usr/bin/env python3

STEPS = 6

def balanced_read(state, dim, pos):
    dx, dy, dz, dq = dim
    x, y, z, q = pos
    return state[dq + q][dz + z][dy + y][dx + x]

def valid_pos(dim, pos):
    dx, dy, dz, dq = dim
    x, y, z, q = pos
    return (x in range(-dx, dx+1)) and (y in range(-dy, dy+1)) and (z in range(-dz, dz+1)) and (q in range(-dq, dq+1))

def expand_state_4d(state, steps):
    height = len(state)
    width = len(state[0])
    assert all(len(row) == width for row in state)
    if width % 2 == 0:
        state = [row + '.' for row in state]
        width += 1
    if height % 2 == 0:
        state.append('.' * width)
        height += 1
        
    assert height % 2 == 1
    assert width % 2 == 1
     
    ix, iy, iz, iq = (width - 1) // 2, (height - 1) // 2, 0, 0
    x, y, z, q = ix + steps, iy + steps, iz + steps, iq + steps
    dim = x, y, z, q
    idim = ix, iy, iz, iq
    xir, yir, zir, qir = range(-ix, ix+1), range(-iy, iy+1), range(-iz, iz+1), range(-iq, iq+1)
    wstate = [[state]]
    return dim, [[[''.join(balanced_read(wstate, idim, (px, py, pz, pq)) if
                          ((px in xir) and (py in yir) and (pz in zir) and (pq in qir)) else '.'
                     for px in range(-x, x+1)) for py in range(-y, y+1)] for pz in range(-z, z+1)] for pq in range(-q, q+1)]

def state_next(state, dim, pos):
    adj_active = 0
    dx, dy, dz, dq = dim
    x, y, z, q = pos
    for cq in range(q-1, q+2):
        for cz in range(z-1, z+2):
            for cy in range(y-1, y+2):
                for cx in range(x-1, x+2):
                    cpos = cx, cy, cz, cq
                    if cpos != pos and valid_pos(dim, cpos) and balanced_read(state, dim, cpos) == '#':
                        adj_active += 1

    current_val = balanced_read(state, dim, pos)
    if current_val == '.':
        if adj_active == 3:
            return '#'
        else:
            return '.'
    elif current_val == '#':
        if adj_active == 2 or adj_active == 3:
            return '#'
        else:
            return '.'
    else:
        raise Exception('unhandled type')

def evolution_step(state, dim):
    dx, dy, dz, dq = dim
    return [[[''.join(state_next(state, dim, (x, y, z, q))
                     for x in range(-dx, dx+1)) for y in range(-dy, dy+1)] for z in range(-dz, dz+1)] for q in range(-dq, dq+1)]

def count_active(state, dim):
    return sum(row.count('#') for cube in state for plane in cube for row in plane)

def solution(lines):
    state_in = list(lines)
    
    dim, state = expand_state_4d(state_in, STEPS)

    for i in range(STEPS):
        state = evolution_step(state, dim)
    
    final_active = count_active(state, dim)
    print(f"Solution: {final_active}")

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
