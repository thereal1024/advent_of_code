#!/usr/bin/env python3

from itertools import zip_longest

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

    ordered_idx_sum = 0
    for i, (left, right) in enumerate(pairs):
        if compare_pkts(left, right) <= 0:
            ordered_idx_sum += i+1
            
    print(f'Solution: {ordered_idx_sum}')
            

if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
