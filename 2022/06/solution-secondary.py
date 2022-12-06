#!/usr/bin/env python3

LEN = 14

def solution(lines):
    msg = next(lines)
    for i in range(0, len(msg)-LEN+1):
        testset = set(msg[i:i+LEN])
        if len(testset) == LEN:
            break
    pos = i + LEN
    print(f'Solution: {pos}')
        

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
