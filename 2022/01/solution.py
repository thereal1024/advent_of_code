#!/usr/bin/env python3

def solution(lines):
    lines = list(lines)
    cal_lists = []
    while '' in lines:
        sep = lines.index('')
        cal_lists.append(int(item) for item in lines[:sep])
        lines = lines[sep+1:]
    cal_lists.append(int(item) for item in lines)
    
    cal_totals = (sum(cal_list) for cal_list in cal_lists)
    largest_total = max(cal_totals)
    print(f'Solution: {largest_total}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
