#!/usr/bin/env python3

# T = low
# F = high

SIG = {
    False: 'high',
    True: 'low',
}

PRESSES = 1000

from collections import defaultdict

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

    pulses = {False: 0, True: 0}
    def broadcast():
        queue = [('button', 'broadcast', True)]
        while len(queue) > 0:
            fromname, name, signal = queue.pop(0)
            pulses[signal] += 1
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
                    
    for _ in range(PRESSES):
        broadcast()
    
    pulseprod = pulses[False] * pulses[True]
    print(f'Solution: {pulseprod}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
