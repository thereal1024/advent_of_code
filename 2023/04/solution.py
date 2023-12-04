#!/usr/bin/env python3

def solution(lines):
    points = 0
    for line in lines:
        _, numbers = line.split(': ')
        winnums, draws = (set(map(int, l.split())) for l in numbers.split(' | '))
        wins = winnums & draws
        numwins = len(wins)
        if numwins > 0:
            points += 2 ** (numwins - 1)

    print('Solution: {}'.format(points))


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
