#!/usr/bin/env python3

from collections import Counter

CARDV = 'J23456789TQKA'
CARDP = '123456789ABCD'

def solution(lines):
    
    hands = []
    for line in lines: 
        cards, bid = line.split()
        bid = int(bid)
        ccards = Counter(cards)
        jokers = ccards['J']
        ccards = sorted(((ct, card) for card, ct in ccards.items() if card != 'J'), key=lambda s: (s[0],CARDV.index(s[1])), reverse=True)
        
        ccode = None
        topn = ccards[0][0] if len(ccards) > 0 else 0
        # optimally for hand type, joker adds to most frequent card
        topn += jokers
        if topn < 5:
            secn = ccards[1][0]
        if topn == 5:
            ccode = '5k'
        elif topn == 4:
            ccode = '4k'
        elif topn == 3 and secn == 2:
            ccode = '3z'
        elif topn == 3:
            ccode = '3k'
        elif topn == 2 and secn == 2:
            ccode = '2p'
        elif topn == 2:
            ccode = '2k'
        elif topn == 1:
            ccode = '1c'
        else:
            raise Exception('bad cards ' + cards)
        postc = ''.join(CARDP[CARDV.index(cd)] for cd in cards)
        postc += '0' * (5 - len(postc))
        ccode += postc
        hands.append((ccode, cards, bid))
        
    # index zero gets rank 1 (worst hand)
    hands.sort(key=lambda h: h[0])
    totalwin = sum((r+1) * bid for r, (_, _, bid) in enumerate(hands))
    print('Solution {}'.format(totalwin))

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
