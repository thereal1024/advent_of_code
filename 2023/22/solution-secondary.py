#!/usr/bin/env python3

def expand_brick(brick):
    s, e = brick
    points = {s}  
    for n, (sp, ep) in enumerate(zip(s, e)):
        if sp != ep:
            if sp > ep:
                sp, ep = ep, sp
            for c in range(sp, ep+1):
                dup = list(s)
                dup[n] = c
                points.add(tuple(dup))
            break
    return points
            

def minz(brick):
    return min(z for _, _, z in brick)

def lower(brick):
    return {(x, y, z-1) for x, y, z in brick}

def solution(lines):
    
    bricks = []
    
    for line in lines:
        s, e = line.split('~')
        s = tuple(map(int, s.split(',')))
        e = tuple(map(int, e.split(',')))
        assert sum(1 for sp, ep in zip(s, e) if sp == ep) >= 2
        bricks.append((s, e))
    
    bricks = [expand_brick(brick) for brick in bricks]
    bricks.sort(key=minz)
    
    grid = {}
    above = {}
    below = {}
    
    def place_brick(brick, bid):
        brickint = set()
        while minz(brick) > 1:
            lowerbrick = lower(brick)
            brickint = set()
            for block in lowerbrick:
                if block in grid:
                    brickint.add(grid[block])
            if len(brickint) > 0:
                break
            brick = lowerbrick
        below[bid] = brickint
        above[bid] = set()
        for bint in brickint:
            above[bint].add(bid)
        for block in brick:
            grid[block] = bid
        
    for n, brick in enumerate(bricks):
        place_brick(brick, n)
      
      
    def fallcount(bid):
        falling = {bid}
        aboves = above[bid]
        while len(aboves):
            nextaboves = set()
            for abovebrick in aboves:
                nextaboves.update(above[abovebrick])

                belowaboves = below[abovebrick]
                if len(belowaboves - falling) == 0:
                    falling.add(abovebrick)
            aboves = nextaboves
        return len(falling) - 1
    
    total = 0
    for bid in above.keys():
        total += fallcount(bid)
    
    print(f'Solution: {total}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
