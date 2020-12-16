#!/usr/bin/env python3

from collections import Counter

GOAL = 2020

def solution(lines):
    numbers = [int(line) for line in lines]
        
    numbers = Counter(numbers)
    for first_number in numbers.keys():
        for second_number in numbers.keys():
            if first_number == second_number and numbers[first_number] < 2:
                continue
            target_number = GOAL - first_number - second_number
            if target_number in numbers.keys():
                multiplicity = 1
                if target_number == first_number:
                    multiplicity += 1
                if target_number == second_number:
                    multiplicity += 1
                if numbers[target_number] < multiplicity:
                    continue
                product = first_number * second_number * target_number
                print(f"Solution {product}")
                return

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
