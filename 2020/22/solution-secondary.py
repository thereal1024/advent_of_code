#!/usr/bin/env python3

def parse_player(playertext, n):
    playerln, *cards = playertext.split('\n')
    assert playerln == f'Player {n}:'
    return [int(card) for card in cards]

def play_game(p1, p2):
    p1, p2 = list(p1), list(p2)
    
    seen_states = set()
    
    while len(p1) > 0 and len(p2) > 0:
        code = tuple(p1), tuple(p2)
        if code in seen_states:
            return 1, p1
        seen_states.add(code)
        
        p1c, p2c = p1.pop(0), p2.pop(0)
        if len(p1) >= p1c and len(p2) >= p2c:
            winr, _ = play_game(p1[:p1c], p2[:p2c])
            p1wins = winr == 1
        else:
            p1wins = p1c > p2c
        
        if p1wins:
            p1.extend([p1c, p2c])
        else:
            p2.extend([p2c, p1c])

    if len(p1) > 0:
        return 1, p1
    elif len(p2) > 0:
        return 2, p2

def solution(sections):
    p1, p2 = (parse_player(pt, i+1) for i, pt in enumerate(sections))
    
    winr, win = play_game(p1, p2)
    score = sum((i+1)*card for i, card in enumerate(reversed(win)))
    print(f'Solution: {score}')

if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
