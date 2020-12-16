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
    terminates = False
    while pgctr not in seen_instr:
        if pgctr == len(program):
            terminates = True
            break
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
    
    return accum, terminates
        

def solution(lines):
    program = compile_program(lines)
    for i in range(len(program)):
        inst, num = program[i]
        if inst == 'acc':
            continue
        derivative_program = list(program)
        if inst == 'nop':
            derivative_program[i] = ('jmp', num)
        elif inst == 'jmp':
            derivative_program[i] = ('nop', num)
        else:
            raise Exception('unknown instruction: ' + inst)
        accum_final, terminates = execute_program(derivative_program)
        if terminates == True:
            print(f"Solution: {accum_final}")
            return

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
