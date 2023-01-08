#!/usr/bin/env python3

MOD = 20201227
SN = 7

def find_loop(pk):
    # inefficient discrete log that is good enough
    acc = 1
    it = 0
    while acc != pk:
        acc = (acc * SN) % MOD
        it += 1
    return it

def solution(lines):
    cardpk, doorpk = (int(line) for line in lines)
    cardloop = find_loop(cardpk)
    enckey = pow(doorpk, cardloop, MOD)
    print(f'Solution: {enckey}')
    
if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
