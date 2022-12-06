#!/usr/bin/env python3

def solution(lines):
    msg = next(lines)
    for i in range(0, len(msg)-3):
        testset = set(msg[i:i+4])
        if len(testset) == 4:
            break
    pos = i + 4
    print(f'Solution: {pos}')
        

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
