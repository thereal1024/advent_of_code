#!/usr/bin/env python3

from functools import cmp_to_key
from itertools import chain, zip_longest

def parse_packet_r(strpkt, i):
    if strpkt[i].isdigit():
        j = i+1
        while j < len(strpkt) and strpkt[j].isdigit():
            j += 1
        return int(strpkt[i:j]), j-i
    elif strpkt[i] == '[':
        j = i+1
        res = []
        while strpkt[j] != ']':
            item, adv = parse_packet_r(strpkt, j)
            res.append(item)
            j += adv
            if strpkt[j] == ',':
                j += 1
            elif strpkt[j] != ']':
                raise Exception(f'unexpected value sep. char {strpkt[i]} at pos {j} in str ${strpkt}$')
        j += 1
        return res, j-i
    else:
        raise Exception(f'unexpected value char {strpkt[i]} at pos {i} in str ${strpkt}$')

def parse_packet(strpkt):
    res, adv = parse_packet_r(strpkt, 0)
    if adv != len(strpkt):
        raise Exception(f'Only consumed {adv} chars of ${strpkt}$')
    return res

# neg -> lt, 0 -> eq, pos -> gt
def compare_pkts(left, right):
    lt, rt = type(left), type(right)
    if lt == rt == int:
        return left - right
    if lt == rt == list:
        for li, ri in zip_longest(left, right):
            if li == None:
                return -1
            elif ri == None:
                return 1
            ic = compare_pkts(li, ri)
            if ic != 0:
                return ic
        return 0
    else:
        if lt == int:
            left = [left]
        elif rt == int:
            right = [right]
        return compare_pkts(left, right)

def solution(sections):
    str_pairs = (section.split('\n') for section in sections)
    pairs = ((parse_packet(left), parse_packet(right)) for left, right in str_pairs)
    packets = list(chain.from_iterable(pairs))
    
    ps1 = [[2]]
    ps2 = [[6]]
    
    packets.extend([ps1, ps2])
    packets.sort(key=cmp_to_key(compare_pkts))
    ps1i = packets.index(ps1) + 1
    ps2i = packets.index(ps2) + 1    
    dec_key = ps1i * ps2i
    print(f'Solution: {dec_key}')
            

if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
