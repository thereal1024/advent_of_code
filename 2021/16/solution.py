#!/usr/bin/env python3

def convert_hex_bin(n):
    return ''.join('{0:04b}'.format(int(c, 16)) for c in n)


def take(code, start, n):
    adv = start + n
    return int(code[start:adv], 2), adv
    

def parse_packet(code, start=0):
    ptr = start
    version, ptr = take(code, ptr, 3)
    tid, ptr = take(code, ptr, 3)
    
    # literal num
    if tid == 4:
        num = 0
        proceed = True
        while proceed:
            proceed, ptr = take(code, ptr, 1)
            num *= 16
            delta, ptr = take(code, ptr, 4)
            num += delta
        return (version, tid, num), ptr
    else:
        ltid, ptr = take(code, ptr, 1)
        countpkt = True
        if ltid == 0:
            bitlen, ptr = take(code, ptr, 15)
            countpkt = False
        else:
            pktlen, ptr = take(code, ptr, 11)
        
        startptr = ptr
        pkts = []
        def done():
            nonlocal countpkt, startptr, ptr, bitlen, pkts, pktlen
            if countpkt:
                return len(pkts) == pktlen
            else:
                return (ptr-startptr) >= bitlen
        
        while not done():
            spkt, ptr = parse_packet(code, ptr)
            pkts.append(spkt)
        
        return (version, tid, pkts), ptr
    
def version_total(pkt):
    version, tid, val = pkt 
    if tid == 4:
        return version
    else:
        return version + sum(version_total(subpkt) for subpkt in val)
    

def solution(lines):
    code = convert_hex_bin(next(lines))
    pkt, _ = parse_packet(code)
    total = version_total(pkt)
    print(f'Solution: {total}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
