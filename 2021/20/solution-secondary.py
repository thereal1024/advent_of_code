#!/usr/bin/env python3

ROUNDS = 50

def parse_enhalg(enhalg):
    enhalg = enhalg.split('\n')
    assert len(enhalg) == 1 and len(enhalg[0]) == 2**9
    enhalg = enhalg[0]
    return {i: '.#'.index(c) for i, c in enumerate(enhalg)}

def parse_image(image):
    image = image.split('\n')
    points = set()
    for y, row in enumerate(image):
        for x, c in enumerate(row):
            if c == '#':
                points.add((y, x))
            else:
                assert c == '.'
    return frozenset(points)

def bounds(image):
    minx = min(x for _, x in image)
    maxx = max(x for _, x in image)
    miny = min(y for y, _ in image)
    maxy = max(y for y, _ in image)
    return minx, maxx, miny, maxy
    
def render_image(image):
    minx, maxx, miny, maxy = bounds(image)
    return '\n'.join(''.join('.#'[(y, x) in image] for x in range(minx, maxx+1)) for y in range(miny, maxy+1))

def enhance_image(image, enhalg, bg):
    minx, maxx, miny, maxy = bounds(image)
    next_image = set()
    for y in range(miny-1, maxy+2):
        for x in range(minx-1, maxx+2):
            c = 0
            for sy in range(y-1, y+2):
                for sx in range(x-1, x+2):
                    c *= 2
                    if sy in range(miny, maxy+1) and sx in range(minx, maxx+1):
                        c += (sy, sx) in image
                    else:
                        c += bg
            if enhalg[c]:
                next_image.add((y, x))
    bg = enhalg[2**9-1 if bg else 0]
    return frozenset(next_image), bg

def solution(sections):
    enhalg, image = sections
    enhalg = parse_enhalg(enhalg)
    image = parse_image(image)
    bg = 0

    for _ in range(ROUNDS):
        image, bg = enhance_image(image, enhalg, bg)
    
    if bg:
        raise Exception('infinite background lit')
    pixelcount = len(image)
    print(f'Solution: {pixelcount}')

if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
