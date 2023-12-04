#!/usr/bin/env python3

def solution(lines):

    lines = list(lines)
    ncards = len(lines)
    cards = [1] * ncards
    
    for cn, line in enumerate(lines):
        _, numbers = line.split(': ')
        winnums, draws = (set(map(int, l.split())) for l in numbers.split(' | '))
        wins = winnums & draws
        numwins = len(wins)
        for icn in range(cn+1, min(cn+1+numwins, ncards)):
            cards[icn] += cards[cn]

    totalcards = sum(cards)

    print('Solution: {}'.format(totalcards))


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
