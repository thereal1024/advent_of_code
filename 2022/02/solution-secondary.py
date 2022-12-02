#!/usr/bin/env python3

P1 = 'ABC'
P2 = 'XYZ'

def score_game(game):
    p1, p2 = game
    shape_score = p2 + 1
    outcome_score = ((p2 - p1 + 1) % 3) * 3
    return shape_score + outcome_score

def plan_game(game):
    p1, goal = game
    p2 = (p1 + goal - 1) % 3
    return score_game((p1, p2))

def solution(lines):
    games = (line.split(' ') for line in lines)
    rps = ((P1.index(game[0]), P2.index(game[1])) for game in games)
    scores = (plan_game(game) for game in rps)
    total_score = sum(scores)
    print(f'Solution: {total_score}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
