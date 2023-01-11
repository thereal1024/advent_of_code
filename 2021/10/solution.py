#!/usr/bin/env python3

CHARS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def find_parse_error(line):
    stack = []
    for c in line:
        if c in CHARS:
            stack.append(CHARS[c])
        elif c in CHARS.values():
            if len(stack) > 0:
                exp = stack.pop()
                if c != exp:
                    return c
            else:
                raise Exception(f'unbalanced line: {line}')
    return None

def solution(lines):
    illg_chars = (find_parse_error(line) for line in lines)
    score = sum(SCORES[char] for char in illg_chars if char is not None)
    print(f'Solution: {score}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
