#!/usr/bin/env python3

# T = low
# F = high

SIG = {
    False: 'high',
    True: 'low',
}

DEST = 'rx'

from collections import defaultdict
import math

def solution(lines):
    
    broadcaster = None
    flipflop = {}
    conjunction = {}
    
    for line in lines:
        name, outputs = line.split(' -> ')
        outputs = outputs.split(', ')
        if name[0] == '%':
            flipflop[name[1:]] = outputs
        elif name[0] == '&':
            conjunction[name[1:]] = outputs
        else:
            assert name == 'broadcaster'
            assert broadcaster == None
            broadcaster = outputs
    
    def conj_init():
        conjstate = defaultdict(dict)
        def add_state(outgoing, incoming_list):
            for incoming in incoming_list:
                if incoming in conjunction:
                    conjstate[incoming][outgoing] = True
        add_state('broadcaster', broadcaster)
        for name, outputs in conjunction.items():
            add_state(name, outputs)
        for name, outputs in flipflop.items():
            add_state(name, outputs)
        return conjstate
    
    def flip_init():
        return {name: False for name in flipflop.keys()}
        
    conjstate, flipstate = conj_init(), flip_init()

    # problem domain restricting and extracting
    assert all(DEST not in outs for outs in flipflop.values())
    destpreinput = []
    for input, outputs in conjunction.items():
        if DEST in outputs:
            assert len(outputs) == 1
            destpreinput.append(input)
    assert len(destpreinput) == 1
    assert all(destpreinput not in outs for outs in flipflop.values())
    relinputs = set()
    for input, outputs in conjunction.items():
        if destpreinput[0] in outputs:
            assert len(outputs) == 1
            relinputs.add(input)

    relpulse = defaultdict(lambda: defaultdict(list))
    def broadcast(n):
        nonlocal relpulse
        queue = [('button', 'broadcast', True)]
        while len(queue) > 0:
            fromname, name, signal = queue.pop(0)
            if name in relinputs:
                relpulse[signal][name].append(n)
            if name == 'broadcast':
                for dest in broadcaster:
                    queue.append((name, dest, signal))
            elif name in flipflop and signal:
                outsig = flipstate[name]
                flipstate[name] = not flipstate[name]
                for dest in flipflop[name]:
                    queue.append((name, dest, outsig))
            elif name in conjunction:
                conjstate[name][fromname] = signal
                outsig = not any(conjstate[name].values())
                for dest in conjunction[name]:
                    queue.append((name, dest, outsig))
            elif name == DEST and signal == True:
                return True
        return False
                    
    presses = 0
    while True:
        presses += 1
        if presses % 1000 == 0:
            if relpulse[True].keys() == relinputs:
                if all(len(pl) >= 10 for pl in relpulse[True].values()):
                    break
        if broadcast(presses):
            # Probably Will not reach here. The cycle detection will work first.
            print(f'Solution: {presses}')
            exit()
    
    cycles = []
    for pl in relpulse[True].values():
        v0 = pl[0]
        # problem domain restriction: cycle aligned to 0 (vals = n, 2n, 3n, ...)
        for n, val in enumerate(pl, 1):
            assert v0*n == val
        cycles.append(v0)
        
    destactivate = math.lcm(*cycles)
    print(f'Solution: {destactivate}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
