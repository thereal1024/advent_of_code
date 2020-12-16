#!/usr/bin/env python3

from collections import Counter

def questions_all(group):
    person_count = len(group)
    questions_count = Counter()
    for person in group:
        for question in set(person):
            questions_count[question] += 1
    questions_all = [qn for qn, ct in questions_count.items() if ct == person_count]
    return sorted(questions_all)
    
def questions_count_all(group):
    qa = questions_all(group)
    return len(qa)

def split_group(group):
    persons = group.split('\n')
    persons = [person.strip() for person in persons if person != '']
    return persons

def solution(groups):
    groups = [split_group(group) for group in groups]
    total_yes = sum(questions_count_all(group) for group in groups)
    print(f"Solution: {total_yes}")

if __name__ == '__main__':
    file_in = open('input.txt')
    groups = file_in.read().split('\n\n')
    solution(groups)
