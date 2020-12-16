#!/usr/bin/env python3

def compile_program(lines):
    program = []
    for line in lines:
        inst, num = line.split(' ')
        program.append((inst, int(num)))
    return program

def execute_program(program):
    pgctr = 0
    accum = 0
    seen_instr = set()
    running = True
    while pgctr not in seen_instr:
        seen_instr.add(pgctr)
        inst, num = program[pgctr]
        if inst == 'acc':
            accum += num
        elif inst == 'jmp':
            pgctr += num - 1
        elif inst == 'nop':
            pass
        else:
            raise Exception('unknown instruction: ' + inst)
        pgctr += 1
    
    return accum
        

def solution(lines):
    program = compile_program(lines)
    accum_final = execute_program(program)
    print(f"Solution: {accum_final}")

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
