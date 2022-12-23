#!/usr/bin/env python3

from collections import defaultdict
import copy
import itertools

SEAMONSTER_CHARS = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""

def parse_seamonster(sm):
    res = set()
    sm = sm.removeprefix('\n').removesuffix('\n').split('\n')
    h, w = len(sm), len(sm[0])
    for y, row in enumerate(sm):
        for x, char in enumerate(row):
            if char == '#':
                res.add((y, x))
    return frozenset(res), h, w

SEAMONSTER = parse_seamonster(SEAMONSTER_CHARS)

def parse_tile(section):
    id_line, *grid = section.split('\n')
    idn = int(id_line.removesuffix(':').split(' ')[1])
    return idn, grid

# flipAdjEdge -> (id, (fy1, fx1), (fy2, fx2))
# (id, (fy, fx)) -> relR, relB, relL, relT)
def edge_map(tiles):
    emap = defaultdict(list)
    for idn, grid in tiles.items():
        top = grid[0]
        bot = grid[-1]
        lef = ''.join(row[0] for row in grid)
        rig = ''.join(row[-1] for row in grid)
        rtop, rbot, rlef, rrig = top[::-1], bot[::-1], lef[::-1], rig[::-1]
        
        a = (idn, (0, 0), (0, 1))
        b = (idn, (0, 0), (1, 0))
        c = (idn, (1, 0), (1, 1))
        d = (idn, (0, 1), (1, 1))
        
        emap[rig].append(a)
        emap[lef].append(a)
        emap[bot].append(b)
        emap[top].append(b)
        emap[rrig].append(c)
        emap[rlef].append(c)
        emap[rbot].append(d)
        emap[rtop].append(d)
        
        emap[(idn, (0, 0))] = (rig, bot, lef, top)
        emap[(idn, (0, 1))] = (lef, rbot, rig, rtop)
        emap[(idn, (1, 0))] = (rrig, top, rlef, bot)
        emap[(idn, (1, 1))] = (rlef, rtop, rrig, rbot)
        
    return emap

def rotr(tup, n):
    assert 0 <= n < 4
    if n == 0:
        return list(tup)
    elif n == 1:
        return [tup[1][::-1], tup[2], tup[3][::-1], tup[0]]
    elif n == 2:
        return [tup[2][::-1], tup[3][::-1], tup[0][::-1], tup[1][::-1]]
    elif n == 3:
        return [tup[3], tup[0][::-1], tup[1], tup[2][::-1]]

def factors(n):
    fac = []
    for i in range(1, n+1):
        if n % i == 0:
            fac.append((i, n//i))
    return fac

def findimglayout(tiles):
    emap = edge_map(tiles)
    
    def search(tilegrid, h, w):
        nonlocal tiles, emap
        if len(tilegrid) == h and len(tilegrid[-1]) == w:
            return tilegrid
        if len(tilegrid[-1]) == w:
            tilegrid.append([])
        y = len(tilegrid) - 1
        x = len(tilegrid[y])
        la, ta = None, None
        rtid, ttid = None, None
        if x > 0:
            rtid, rf, rr = tilegrid[y][x-1]
            la = rotr(emap[(rtid, rf)], rr)[0] # read rig to match left
        if y > 0:
            ttid, tf, tr = tilegrid[y-1][x]
            ta = rotr(emap[(ttid, tf)], tr)[1] # read bottom to match top
        for idn, fl1, fl2 in emap[la or ta]:
            if idn in (rtid, ttid):
                continue
            for fl in [fl1, fl2]:
                for roti in range(4):
                    _, _, lc, tc = rotr(emap[(idn, fl)], roti)
                    if (lc == (la or lc)) and (tc == (ta or tc)):
                        ntg = copy.deepcopy(tilegrid)
                        ntg[-1].append((idn, fl, roti))
                        res = search(ntg, h, w)
                        if res:
                            return res
        return None
    
    for h, w in factors(len(tiles)):
        for tilen in tiles:
            tilegrid = [[(tilen, (0, 0), 0)]]
            res = search(tilegrid, h, w)
            if res:
                return res

def printgrid(grid):
    print('\n'.join(grid))

def gettile(tiles, spec):
    idn, (fy, fx), rot = spec
    tile = tiles[idn]
    
    tilemod = [row[1:-1] for row in tile[1:-1]]
    
    if fy:
        tilemod = tilemod[::-1]
    if fx:
        tilemod = [row[::-1] for row in tilemod]
    
    for _ in range(rot):
        tilemod = list(reversed(list(map(lambda x: ''.join(x), zip(*tilemod)))))
    
    return tilemod

def getimg(tiles, imgplan):
    h, w = len(imgplan), len(imgplan[0])
    first = next(iter(tiles.values()))
    th = len(first) - 2
    
    img = []
    for row in imgplan:
        rowimg = [''] * th
        for item in row:
            itemimg = gettile(tiles, item)
            for i, itemrow in enumerate(itemimg):
                rowimg[i] += itemrow
        img.extend(rowimg)
    return img

def getimgtfs(img):
    imgtfs = []

    # don't follow redundant rotations only need 2
    for fx, fy, rot in itertools.product([False, True], [False, True], range(2)):        
        imgmod = img
        
        if fy:
            imgmod = imgmod[::-1]
        if fx:
            imgmod = [row[::-1] for row in imgmod]
        
        for _ in range(rot):
            imgmod = list(reversed(list(map(lambda x: ''.join(x), zip(*imgmod)))))

        imgtfs.append(imgmod)

    return imgtfs


def roughness(img):
    smimg, smh, smw = SEAMONSTER
    
    imgpoints = set()
    for y, row in enumerate(img):
        for x, c in enumerate(row):
            if c == '#':
                imgpoints.add((y, x))
    
    smpoints = set()
    for y, row in enumerate(img):
        for x, c in enumerate(row):
            offsetsm = set((y+dy, x+dx) for dy, dx in smimg)
            if offsetsm.issubset(imgpoints):
                smpoints |= offsetsm
                
    if len(smpoints) == 0:
        return -1
    
    return len(imgpoints - smpoints)

def anyrotroughness(img):
    imgtfs = getimgtfs(img)
    rtfs = [roughness(img) for img in imgtfs]
    rn, *rest = sorted(rtfs, reverse=True)
    assert all(e == -1 for e in rest)
    return rn


def solution(sections):
    tiles = dict(parse_tile(section) for section in sections)
    imgplan = findimglayout(tiles)
    img = getimg(tiles, imgplan)
    soln = anyrotroughness(img)
    print(f'Solution: {soln}')

if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
