#!/usr/bin/env python3

from collections import namedtuple
import functools
from tqdm import tqdm

TIME = 24

Blueprint = namedtuple('Blueprint', ['id', 'costs'])

def parse_blueprint(line):
    tok = line.split(' ')
    ore = (int(tok[6]), 0, 0, 0)
    clay = (int(tok[12]), 0, 0, 0)
    obs = (int(tok[18]), int(tok[21]), 0, 0)
    geo = (int(tok[27]), 0, int(tok[30]), 0, 0)
    return Blueprint(
        id=int(tok[1][:-1]),
        costs=[ore, clay, obs, geo]
    )

def most_geo(bp, time):
    max_items = tuple(max(mat) for mat in zip(*bp.costs, (0, 0, 0, float('inf'))))
    
    @functools.cache
    def geo_rec(bots, mats, time):
        nonlocal bp, max_items

        if time == 0:
            return mats[3]
        
        after_build = [(bots, mats)]
        
        for bot_i, recipe in enumerate(bp.costs):
            # do not need more bots of type than maximum material type needed in a tick
            if bots[bot_i] >= max_items[bot_i]:
                continue
            if all(matamt >= reccost for matamt, reccost in zip(mats, recipe)):
                newbots = tuple(botc + (i == bot_i) for i, botc in enumerate(bots))
                newmats = tuple(matamt - reccost for matamt, reccost in zip(mats, recipe))
                after_build.append((newbots, newmats))
        
        best = 0
        for newbots, newmats in after_build:
            newmats = tuple(min(matamt + botc, time * maxi) for matamt, botc, maxi in zip(newmats, bots, max_items))
            best = max(best, geo_rec(newbots, newmats, time - 1))
        
        return best
    
    return geo_rec((1, 0, 0, 0), (0, 0, 0, 0), time)

def solution(lines):
    blueprints = [parse_blueprint(line) for line in lines]
    geos = [(bp.id, most_geo(bp, TIME)) for bp in tqdm(blueprints)]
    soln = sum(idn * score for idn, score in geos)
    print(f'Solution: {soln}')

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
