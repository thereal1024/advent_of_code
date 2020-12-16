#!/usr/bin/env python3

GOAL = 2020

def solution(lines):
    numbers = [int(line) for line in lines]
    
    if numbers.count(GOAL/2) > 1:
        product = GOAL**2
        print(f"Solution {product}")
        
    numbers = set(numbers)
    for number in numbers:
        if (GOAL - number) in numbers:
            product = number * (GOAL - number)
            print(f"Solution {product}")
            break

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
