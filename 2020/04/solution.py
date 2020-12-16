#!/usr/bin/env python3

COUNTRY_ITEM = 'cid'
ITEM_NAMES = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', COUNTRY_ITEM]

def valid_item(item):
    valid = item[0] in ITEM_NAMES
    return valid

def validate_passport(passport):
    lines = passport.split('\n')
    items = [item.split(':') for line in lines for item in line.strip().split(' ')]
    return sum(valid_item(item) for item in items if item[0] != COUNTRY_ITEM) == len(ITEM_NAMES) - 1

def solution(passports):
    valid_passports = sum(validate_passport(passport) for passport in passports)
    print(f"Solution: {valid_passports}")

if __name__ == '__main__':
    file_in = open('input.txt')
    passports = file_in.read().split('\n\n')
    solution(passports)
