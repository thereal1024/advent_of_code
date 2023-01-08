#!/usr/bin/env python3

def parse_player(playertext, n):
    playerln, *cards = playertext.split('\n')
    assert playerln == f'Player {n}:'
    return [int(card) for card in cards]

def play_and_score_game(p1, p2):
    p1, p2 = list(p1), list(p2)
    
    while len(p1) > 0 and len(p2) > 0:
        p1c, p2c = p1.pop(0), p2.pop(0)
        if p1c > p2c:
            p1.extend([p1c, p2c])
        elif p2c > p1c:
            p2.extend([p2c, p1c])
        else:
            raise Exception(f'equal cards {p1c} {p2c}')
            
    if len(p1) > 0:
        win = p1
        winr = 1
    elif len(p2) > 0:
        win = p2
        winr = 2
    else:
        raise Exception('both hands empty')
    
    score = sum((i+1)*card for i, card in enumerate(reversed(win)))
    return winr, score
    

def solution(sections):
    p1, p2 = (parse_player(pt, i+1) for i, pt in enumerate(sections))
    
    winp, score = play_and_score_game(p1, p2)
    print(f'Solution: {score}')

if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
