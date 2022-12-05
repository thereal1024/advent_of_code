#!/usr/bin/env python3

from collections import deque

def parse_move(movestr):
    tokens = movestr.split(' ')
    return (int(tokens[1]), int(tokens[3])-1, int(tokens[5])-1)

def solution(sections):
    crates, moves = sections
    crates = crates.split('\n')[:-1]
    cols = (len(crates[0])+1) // 4
    height = len(crates)
    
    cratescols = [deque() for i in range(cols)]
    for col in range(cols):
        for ht in range(height):
            val = crates[ht][col*4+1]
            if val != ' ':
                cratescols[col].appendleft(val)

    moves = moves.split('\n')[:-1]
    moves = (parse_move(move) for move in moves)
    
    for count, src, dst in moves:
        carry = deque()
        for _ in range(count):
            carry.appendleft(cratescols[src].pop())
        cratescols[dst].extend(carry)
    
    solution = ''.join(cratecol[-1] for cratecol in cratescols)
    print(f'Solution: {solution}')
    

if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().split('\n\n')
    solution(sections)
