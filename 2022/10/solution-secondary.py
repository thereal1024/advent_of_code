#!/usr/bin/env python3

WIDTH = 40

def solution(lines):
    
    cycle = 1
    x = 1
    
    picture = ['']
    
    def drawpixel():
        nonlocal picture
        h = (cycle - 1) % WIDTH
        
        if x-1 <= h <= x+1:
            c = '#'
        else:
            c = '.'
        picture[-1] += c
        
        if h == WIDTH -1:
            picture.append('')
    
    for op in lines:
        if op == 'noop':
            drawpixel()
            cycle += 1
        elif op.startswith('addx'):
            incr = int(op.removeprefix('addx '))
            drawpixel()
            cycle += 1
            drawpixel()
            cycle += 1
            x += incr
        else:
            raise Exception(f'unknown op: {op}')
    
    picture.pop() # drop unfilled line
    print(f'Solution:')
    for line in picture:
        print(line)

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
