#!/usr/bin/env python3

from functools import lru_cache

def solution(lines):
    ordered_adapters = [0] + sorted(int(num) for num in lines)
    ordered_adapters += [ordered_adapters[-1] + 3]
    diff_list = [ordered_adapters[i+1] - ordered_adapters[i] for i in range(len(ordered_adapters) - 1)]
    
    assert all(e in range(1, 4) for e in diff_list)
    
    @lru_cache(maxsize=len(diff_list))
    def count_solns(i=0):
        if i == len(diff_list) - 1:
            return 1
        first = diff_list[i]
        assert first <= 3
        solns = count_solns(i + 1)
        second = diff_list[i + 1] if i < len(diff_list) - 1 else 3
        second_prefix = first + second
        if second_prefix > 3:
            return solns
        solns += count_solns(i + 2)
        third = diff_list[i + 2] if i < len(diff_list) - 2 else 3
        third_prefix = second_prefix + third
        if third_prefix > 3:
            return solns
        solns += count_solns(i + 3)
        return solns
    
    solns = count_solns()
    print(f"Solution: {solns}")
    
if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
