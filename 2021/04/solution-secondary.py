#!/usr/bin/env python3

SIDE = 5

def make_tests():
    tests = []
    for i in range(SIDE):
        tests.append(tuple(range(i*SIDE, (i+1)*SIDE)))
    q = range(0, SIDE*SIDE, SIDE)
    for i in range(SIDE):
        tests.append(tuple(e+i for e in q))
    return tests

TESTS = make_tests()

def parse_board(lines):
    board = tuple(map(int, lines.split()))
    return board

def run_game_last(boards, nums):
    
    marks = [dict((i, False) for i in range(SIDE**2)) for _ in range(len(boards))]
    
    for num in nums:
        for board, mark in zip(boards, marks):
            if num in board:
                pos = board.index(num)
                mark[pos] = True
        
        winners = []
        for board, mark in zip(boards, marks):
            for test in TESTS:
                if all(mark[e] for e in test):
                    winners.append((board, mark))
                    break
                
        if winners:
            if len(boards) > 1:
                for board, mark in winners:
                    boards.remove(board)
                    marks.remove(mark)
                assert len(boards) > 0
            else:
                board, mark = winners[0]
                score = sum(board[i] for i in range(SIDE*SIDE) if not mark[i])
                score *= num
                return score
                
def solution(sections):
    nums, *boards = sections
    nums = list(map(int, nums.split(',')))
    boards = [parse_board(board) for board in boards]
    win_score = run_game_last(boards, nums)
    print(f'Solution: {win_score}')    
    
if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
