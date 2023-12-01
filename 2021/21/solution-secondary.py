#!/usr/bin/env python3

import functools
import itertools

DICE_SIDES = 3
DIE_ROLLS = 3
SPACES = 10
END_SCORE = 21

def parse_players(lines):
    p1l, p2l = lines
    p1 = int(p1l.removeprefix('Player 1 starting position: ')) - 1
    p2 = int(p2l.removeprefix('Player 2 starting position: ')) - 1
    return p1, p2

def adj_pos(pos, total):
    return (pos + total) % SPACES

@functools.cache
def game_wins(positions, scores=(0, 0), turn=0):    
    wins = (0, 0)
    for r1, r2, r3 in itertools.product(range(1, DICE_SIDES + 1), repeat=3):
        total = r1 + r2 + r3
        if turn == 0:
            sub_positions = (adj_pos(positions[0], total), positions[1])
            sub_scores = (scores[0] + sub_positions[0] + 1, scores[1])
            win_now = sub_scores[0] >= END_SCORE
        else:
            sub_positions = (positions[0], adj_pos(positions[1], total))
            sub_scores = (scores[0], scores[1] + sub_positions[1] + 1)
            win_now = sub_scores[1] >= END_SCORE
        if not win_now:
            next_turn = (turn + 1) % len(positions)
            sub_wins = game_wins(sub_positions, sub_scores, next_turn)
            wins = (wins[0] + sub_wins[0], wins[1] + sub_wins[1])
        else:
            winner = (1-turn, turn)
            wins = (wins[0] + winner[0], wins[1] + winner[1])
 
    return wins

def solution(lines):
    p1, p2 = parse_players(lines)
    win1, win2 = game_wins((p1, p2))
    winner_wins = max(win1, win2)
    print(f'Solution: {winner_wins}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
