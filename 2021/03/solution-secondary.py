#!/usr/bin/env python3

def filter(num_strs, most):
    bits = len(num_strs[0])
    for i in range(bits):
        if len(num_strs) == 1:
            break
        items = len(num_strs)
        
        count_ones = 0
        for num_str in num_strs:
            if num_str[i] == '1':
                count_ones += 1
                
        if count_ones > items / 2:
            maj_digit = '1'
        elif count_ones == items / 2:
            maj_digit = '1'
        else:
            maj_digit = '0'
            
        keep_digit = maj_digit if most else '10'[int(maj_digit)]
        num_strs = [num_str for num_str in num_strs if num_str[i] == keep_digit]
    
    if len(num_strs) != 1:
        raise Exception('failed filter')
    
    return int(num_strs[0], 2)
    

def solution(lines):
    lines = list(lines)
    oxr = filter(lines, True)
    cor = filter(lines, False)
    soln = oxr * cor
    print(f"Solution: {soln}")
    
if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
