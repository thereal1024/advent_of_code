#!/usr/bin/env python3

from collections import Counter

def parse_scanner(scannerlines, n):
    header, *rest = scannerlines.split('\n')
    assert header == f'--- scanner {n} ---'
    return [tuple(map(int, bec.split(','))) for bec in rest]

def rotate_x(x, y, z):
    return x, -z, y

def rotate_y(x, y, z):
    return z, y, -x

def point_rotations(p):
    rotations = []
    for _ in range(2):
        for _ in range(3):
            p = rotate_x(*p)
            rotations.append(p)
            for _ in range(3):
                p = rotate_y(*p)
                rotations.append(p)
        p = rotate_x(*rotate_y(*rotate_x(*p)))
    return rotations

def list_rotations(pts):
    rot_by_pt = [point_rotations(p) for p in pts]
    return list(zip(*rot_by_pt))

def remove_offset_from_list(pts, offset):
    dx, dy, dz = offset
    return [(x-dx, y-dy, z-dz) for x, y, z in pts]

def align_scanner(base_bec, scanner):
    for scanrot in list_rotations(scanner):
        comb_offsets = ((sx - bx, sy - by, sz - bz)
                        for bx, by, bz in base_bec for sx, sy, sz in scanrot)
        [(offset, count)] = Counter(comb_offsets).most_common(1)
        if count >= 12:
            return remove_offset_from_list(scanrot, offset), offset
    return None, None

def beacon_count(scanners):
    scan_q = list(enumerate(scanners))
    _, base_bec = scan_q.pop(0)
    base_bec = set(base_bec)
    scan_locs = {0: (0, 0, 0)}
    
    while len(scan_q) > 0:
        n, scanner = scan_q.pop(0)
        maybe_aligned, scan_loc = align_scanner(base_bec, scanner)
        if maybe_aligned:
            base_bec |= set(maybe_aligned)
            scan_locs[n] = scan_loc
        else:
            scan_q.append((n, scanner))

    return len(base_bec)

def solution(sections):
    scanners = [parse_scanner(section, i) for i, section in enumerate(sections)]
    beacons = beacon_count(scanners)
    print(f'Solution: {beacons}')

if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
