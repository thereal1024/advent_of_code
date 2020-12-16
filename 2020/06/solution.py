#!/usr/bin/env python3

def questions_any(group):
    questions = set()
    for person in group:
        questions.update(iter(person))
    return sorted(questions)
    
def questions_count_any(group):
    qa = questions_any(group)
    return len(qa)

def split_group(group):
    persons = group.split('\n')
    persons = [person.strip() for person in persons if person != '']
    return persons

def solution(groups):
    groups = [split_group(group) for group in groups]
    total_yes = sum(questions_count_any(group) for group in groups)
    print(f"Solution: {total_yes}")

if __name__ == '__main__':
    file_in = open('input.txt')
    groups = file_in.read().split('\n\n')
    solution(groups)
