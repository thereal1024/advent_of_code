#!/usr/bin/env python3

import re

TEMPLATE = """
(?:inp w
mul x 0
add x z
mod x 26
div z (1|26)
add x (-?\d+)
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y (\d+)
mul y x
add z y
)
""".strip()

# for push, [add | comp], input in code:
#   if push:
#     s.push(input + add)
#   else:
#     assert s.pop() + comp == input
#
# returns list of (push, [add | comp]
def validate_params(params):
    out_params = []
    s, sm = 0, 0
    for div, comp, add in params:
        if div == 1:
            assert comp > 9
            out_params.append((True, add))
            s += 1
            sm += 1
        else:
            out_params.append((False, comp))
            s -= 1
        assert s >= 0
    assert s == 0
    assert sm == len(params) // 2
    return out_params
            
def balance(delta):
    if delta > 0:
        return 1, 1 + delta
    else:
        return 1 - delta, 1

def solve_params(params):
    stack = []
    out = {}
    for i, (push, n) in enumerate(params):
        if push:
            stack.append((i, n))
        else:
            pi, pn = stack.pop()
            sp, s = balance(pn + n)
            out[pi] = sp
            out[i] = s
    return int(''.join(str(out[i]) for i in range(len(params))))

def solution(code):
    if not re.fullmatch(TEMPLATE+'+', code):
        raise Exception('bad input')
    
    params = re.findall(TEMPLATE, code)
    params = [tuple(map(int, e)) for e in params]
    params = validate_params(params)
    model = solve_params(params)
    print(f'Solution: {model}')
    

if __name__ == '__main__':
    file_in = open('input.txt')
    code = file_in.read()
    solution(code)
