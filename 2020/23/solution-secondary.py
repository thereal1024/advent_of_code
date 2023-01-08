#!/usr/bin/env python3

ROUNDS = 10000000
COUNT = 1000000
LOW = 1
HIGH = COUNT

def solution(lines):
    cups = [int(c) for c in next(lines)]
    
    cups += list(range(len(cups)+1, COUNT+1))
    
    cursor = cups[0]
    cups = dict(zip(cups, cups[1:] + [cups[0]]))
    
    for _ in range(ROUNDS):
        next1 = cups[cursor]
        next2 = cups[next1]
        next3 = cups[next2]
        taken = [next1, next2, next3]
        dest = cursor - 1
        while dest in taken or dest < LOW:
            dest -= 1
            if dest < LOW:
                dest = HIGH
        # remove all of taken
        cups[cursor] = cups[taken[-1]]
        # insert taken (connect end then beginning)
        cups[taken[-1]] = cups[dest]
        cups[dest] = taken[0]
        # advance cursor
        cursor = cups[cursor]

    l1, l2 = cups[1], cups[cups[1]]
    soln = l1 * l2
    print(f'Solution: {soln}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
