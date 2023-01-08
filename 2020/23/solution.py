#!/usr/bin/env python3

ROUNDS = 100
LOW = 1
HIGH = 9

def solution(lines):
    cups = [int(c) for c in next(lines)]
    
    for _ in range(ROUNDS):
        cur = cups[0] - 1
        taken = [cups.pop(1), cups.pop(1), cups.pop(1)]
        while cur not in cups:
            cur -= 1
            if cur < LOW:
                cur = HIGH
        dest = cups.index(cur)
        cups = cups[:dest+1] + taken + cups[dest+1:]
        front = cups.pop(0)
        cups.append(front)

    onei = cups.index(1)
    labels = cups[onei+1:] + cups[:onei]
    labels = ''.join(str(label) for label in labels)
    print(f'Solution: {labels}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
