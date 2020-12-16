#!/usr/bin/env python3

def solution(lines):
    lines = list(lines)
    clock_start = int(lines[0])
    bus_times = sorted(int(e) for e in lines[1].split(',') if e != 'x')
    
    for time in range(clock_start, clock_start + max(bus_times)):
        for bus_time in bus_times:
            if time % bus_time == 0:
                idn = bus_time
                wait = time - clock_start
                soln = idn * wait
                print(f"Solution: {soln}")
                return

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
