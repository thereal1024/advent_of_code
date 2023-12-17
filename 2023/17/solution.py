#!/usr/bin/env python3

import heapq

# dy, dx
# RLDU
DIRS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

OPPOSITE = {
    (0, 0): (0, 0),
    DIRS[0]: DIRS[1],
    DIRS[1]: DIRS[0],
    DIRS[2]: DIRS[3],
    DIRS[3]: DIRS[2],
}

def solution(lines):
    lines = list(lines)
    h, w = len(lines), len(lines[0])
    
    heatloss = {}
    
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            heatloss[(y, x)] = int(c)

    def valid_moves(state):
        point, direc, repeat = state
        moves = []
        for delta in DIRS:
            if direc == delta and repeat == 3:
                continue
            if OPPOSITE[direc] == delta:
                continue
            newpoint = point[0] + delta[0], point[1] + delta[1]
            if newpoint[0] not in range(h) or newpoint[1] not in range(w):
                continue
            
            if direc == delta:
                newrepeat = repeat + 1
            else:
                newrepeat = 1
            newstate = newpoint, delta, newrepeat
            inccost = heatloss[newpoint]
            moves.append((inccost, newstate))
        return moves
        

    costs = {}
    queue = []
    # cost, (point, direc, repeat)
    heapq.heappush(queue, (0, ((0, 0), (0, 0), 0)))
    while len(queue) > 0:
        cost, state = heapq.heappop(queue)
        
        if state in costs:
            continue
        
        costs[state] = cost
        for inccost, newstate in valid_moves(state):
            if newstate not in costs:
                heapq.heappush(queue, (cost + inccost, newstate))
                
    finaldest = h-1, w-1

    leastloss = min(cost for (point, _, _), cost in costs.items() if point == finaldest)
    print(f'Solution: {leastloss}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
