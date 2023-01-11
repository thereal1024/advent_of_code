#!/usr/bin/env python3

from statistics import median

CHARS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

SCORES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def get_line_completion(line):
    stack = []
    for c in line:
        if c in CHARS:
            stack.append(CHARS[c])
        elif c in CHARS.values():
            if len(stack) > 0:
                exp = stack.pop()
                if c != exp:
                    return None
            else:
                raise Exception(f'unbalanced line: {line}')
    return ''.join(reversed(stack))

def score_completion(comp):
    score = 0
    for c in comp:
        score *= 5
        score += SCORES[c]
    return score

def solution(lines):
    line_completions = (get_line_completion(line) for line in lines)
    scores = [score_completion(comp) for comp in line_completions if comp is not None]
    mscore = median(scores)
    print(f'Solution: {mscore}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
