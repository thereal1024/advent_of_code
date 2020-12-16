#!/usr/bin/env python3

MAX_SEAT = 896

def valid_pass(bp):
    len(bp) == 10
    return all(char in 'FB'for char in bp[:7]) and all (char in 'LR' for char in bp[7:])

def decode_bpass(bp):
    assert valid_pass(bp)
    rowcode = int(bp[:7].replace('F', '0').replace('B', '1'), 2)
    colcode = int(bp[7:].replace('L', '0').replace('R', '1'), 2)
    return rowcode, colcode

def code_to_id(code):
    rowcode, colcode = code
    return rowcode * 8 + colcode

def solution(lines):
    seats_available = set(range(MAX_SEAT + 1))
    
    codes_found = (code_to_id(decode_bpass(line)) for line in lines)
    for code in codes_found:
        seats_available.remove(code)

    for i in range(MAX_SEAT):
        if i not in seats_available:
            min_seat = i
            break
            
    for i in range(MAX_SEAT, -1, -1):
        if i not in seats_available:
            max_seat = i + 1
            break

    seats_available = {seat for seat in seats_available if seat in range(min_seat, max_seat)}
    assert len(seats_available) == 1
    seat = next(iter(seats_available))
    print(f"Solution: {seat}")

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
