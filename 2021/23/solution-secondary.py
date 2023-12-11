#!/usr/bin/env python3

from collections import defaultdict
import heapq

INS = ['DCBA', 'DBAC']

COSTS = {c: 10**i for i, c in enumerate('ABCD')}
DELTAS = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1]
]

def enhance(lines):
    for i, line in enumerate(lines):
        if any(c.isalpha() for c in line):
            break
    
    apos = min(i for i, c in enumerate(line) if c.isalpha())
    extra = []
    for order in INS:
        #'012A' # 3
        s = ' ' * (apos - 1) + '#'
        for c in order:
            s += c + '#'
        s += ' ' * (apos - 1)
        extra.append(s)
    newlines = lines[:(i+1)] + extra + lines[(i+1):]
    return newlines

def adjacent(pos):
    y, x = pos
    return [(y+dy, x+dx) for dy, dx in DELTAS]

def solution(lines):
    spaces = set()
    walls = set() # for printing
    positions = set()
    
    lines = list(lines)
    lines = enhance(lines)
    h, w = len(lines), max(len(line) for line in lines)
    
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c == '.' or c in COSTS.keys():
                spaces.add((y, x))
            elif c == '#':
                walls.add((y, x))
            if c in COSTS.keys():
                positions.add(((y, x), c))
    positions = frozenset(positions)
    
    def printboard(pos):
        nonlocal spaces, walls, h, w
        out = ''
        posdict = {p: c for p, c in pos}
        for y in range(h):
            for x in range(w):
                coord = y, x
                if coord in posdict:
                    out += posdict[coord]
                elif coord in walls:
                    out += '#'
                elif coord in spaces:
                    out += '.'
                else:
                    out += ' '
            out += '\n'
        print(out, end='')
    
    # final goal
    goalpos = set()
    dests = defaultdict(list)
    ys, xs = set(), set()
    for (y, x), _ in positions:
        ys.add(y)
        xs.add(x)
    assert len(ys) * len(xs) == len(positions)
    assert len(ys) == max(ys) - min(ys) + 1
    for x, c in zip(sorted(xs), COSTS.keys()):
        for y in sorted(ys):
            goalpos.add(((y, x), c))
    goalpos = frozenset(goalpos)

    # classifying spaces
    hallways = set(spaces)
    for (y, x), c in goalpos:
        dests[c].append((y, x))
        hallways.remove((y, x))
    hallwayy = min(y for y, _ in hallways)
    assert all(y == hallwayy for y, _ in hallways)
    for x in xs:
        hallways.remove((hallwayy, x))
    for l in dests.values():
        l.sort()
   
    def valid_moves(pos):
        head = {}
        op = {}
        for c, pl in dests.items():
            head[c] = None
            op[c] = None
            clean = True
            found = False
            first = None
            avail = None
            for p in pl:
                for ci in COSTS.keys():
                    if (p, ci) in pos:
                        if not found:
                            first = p
                            found = True
                        if c != ci:
                            clean = False
                if not found:
                    avail = p
            if clean:
                op[c] = avail
            else:
                head[c] = first

        blocked = set(coord[1] for coord, c in pos if coord in hallways)
        
        def blk(s, e):
            if abs(e[1] - s[1]) <= 1:
                return False
            lx, rx = sorted([e[1], s[1]])
            lx, rx = lx+1, rx-1
            return any(x in blocked for x in range(lx, rx+1))
        
        def opn(s):
            dst = []
            for x in range(s[1]-1, -1, -1):
                if x in blocked:
                    break
                d = (hallwayy, x)
                if d in hallways:
                    dst.append(d)
            for x in range(s[1]+1, w):
                if x in blocked:
                    break
                d = (hallwayy, x)
                if d in hallways:
                    dst.append(d)
            return dst

        poslist = []
        for coord, c in pos:
            if coord in hallways and op[c] != None:
                dest = op[c]
                if blk(coord, dest):
                    continue
                md = abs(dest[0] - coord[0]) + abs(dest[1] - coord[1])
                cost = COSTS[c] * md
                newpos = set(pos)
                newpos.remove((coord, c))
                newpos.add((dest, c))
                poslist.append((frozenset(newpos), cost))
            elif coord in head.values():
                for dest in opn(coord):
                    md = abs(dest[0] - coord[0]) + abs(dest[1] - coord[1])
                    cost = COSTS[c] * md
                    newpos = set(pos)
                    newpos.remove((coord, c))
                    newpos.add((dest, c))
                    poslist.append((frozenset(newpos), cost))
        return poslist
    
    costs = {}
    queue = []
    heapq.heappush(queue, (0, positions))
    while goalpos not in costs:
        cost, node = heapq.heappop(queue)
        
        if node in costs:
            continue
        
        costs[node] = cost
        for newnode, inccost in valid_moves(node):
            if newnode not in costs:
                heapq.heappush(queue, (cost + inccost, newnode))


    overallmin = costs[goalpos]
    print('Solution: {}'.format(overallmin))
            

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip('\n') for line in file_in.readlines())
    solution(lines)
