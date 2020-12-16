#!/usr/bin/env python3

import string

# helper functions
num_string = lambda s: all(char in string.digits for char in s)
strict_num_string = lambda s: not s.startswith('0') and num_string(s)
valid_range = lambda n, first, last: n in range(first, last + 1)
valid_cm_height = lambda s: s.endswith('cm') and strict_num_string(s[:-2]) and valid_range(int(s[:-2]), 150, 193)
valid_in_height = lambda s: s.endswith('in') and strict_num_string(s[:-2]) and valid_range(int(s[:-2]), 59, 76)

# validator functions
valid_birth_year = lambda yrs: strict_num_string(yrs) and valid_range(int(yrs), 1920, 2002)
valid_issue_year = lambda yrs: strict_num_string(yrs) and valid_range(int(yrs), 2010, 2020)
valid_exp_year = lambda yrs: strict_num_string(yrs) and valid_range(int(yrs), 2020, 2030)
valid_height = lambda hs: valid_cm_height(hs) or valid_in_height(hs)
valid_hair = lambda hc: hc.startswith('#') and len(hc) == 7 and all(char in string.hexdigits for char in hc[1:])
valid_eye = lambda es: es in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
valid_passport = lambda pp: len(pp) == 9 and num_string(pp)
valid_country = lambda c: True

COUNTRY_ITEM = 'cid'
ITEM_VALIDATORS = {'byr': valid_birth_year,
                   'iyr': valid_issue_year,
                   'eyr': valid_exp_year,
                   'hgt': valid_height,
                   'hcl': valid_hair,
                   'ecl': valid_eye,
                   'pid': valid_passport,
                   COUNTRY_ITEM: valid_country}

def valid_item(item):
    valid = item[0] in ITEM_VALIDATORS
    if not valid:
        return False
    return ITEM_VALIDATORS[item[0]](item[1])

def validate_passport(passport):
    lines = passport.split('\n')
    items = [item.split(':') for line in lines for item in line.strip().split(' ')]
    return sum(valid_item(item) for item in items if item[0] != COUNTRY_ITEM) == len(ITEM_VALIDATORS) - 1

def solution(passports):
    valid_passports = sum(validate_passport(passport) for passport in passports)
    print(f"Solution: {valid_passports}")
    pass

if __name__ == '__main__':
    file_in = open('input.txt')
    passports = file_in.read().split('\n\n')
    solution(passports)
