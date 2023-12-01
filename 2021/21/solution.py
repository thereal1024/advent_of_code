#!/usr/bin/env python3

import itertools

DICE_SIDES = 100
DIE_ROLLS = 3
SPACES = 10
END_SCORE = 1000

def parse_players(lines):
    p1l, p2l = lines
    p1 = int(p1l.removeprefix('Player 1 starting position: ')) - 1
    p2 = int(p2l.removeprefix('Player 2 starting position: ')) - 1
    return p1, p2

def make_die():
    return itertools.cycle(range(1, DICE_SIDES + 1))

def game(p1, p2):
    players = [p1, p2]
    scores = [0, 0]
    player_turns = itertools.cycle(range(2))
    
    die = make_die()
    roll_count = 0
    
    def get_roll_total():
        nonlocal die, roll_count
        rolls = [next(die) for _ in range(DIE_ROLLS)]
        roll_count += len(rolls)
        return sum(rolls)
    
    while True:
        player_up = next(player_turns)
        total = get_roll_total()
        players[player_up] = (players[player_up] + total) % SPACES
        scores[player_up] += players[player_up] + 1
        if scores[player_up] >= END_SCORE:
            break
    
    return min(scores) * roll_count

def solution(lines):
    p1, p2 = parse_players(lines)
    fscoreprod = game(p1, p2)
    print(f'Solution: {fscoreprod}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
