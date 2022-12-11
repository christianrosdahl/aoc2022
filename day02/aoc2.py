# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Advent of Code 2022 - Day 2

# + tags=[]
file = open('input2.txt','r')
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')


# -

def points(opponent_action, my_action):
    points = 0
    # Points for chosen action
    if my_action == 'X':
        points += 1
    elif my_action == 'Y':
        points += 2
    elif my_action == 'Z':
        points += 3
    
    # Points for outcome
    if opponent_action == 'A':
        if my_action == 'X':
            points += 3
        elif my_action == 'Y':
            points += 6
        elif my_action == 'Z':
            points += 0
    elif opponent_action == 'B':
        if my_action == 'X':
            points += 0
        elif my_action == 'Y':
            points += 3
        elif my_action == 'Z':
            points += 6
    elif opponent_action == 'C':
        if my_action == 'X':
            points += 6
        elif my_action == 'Y':
            points += 0
        elif my_action == 'Z':
            points += 3
    return points


total_points = 0
for line in lines:
    opponent_action, my_action = line.split()
    total_points += points(opponent_action, my_action)
print('Total points: ' + str(total_points))


def points2(opponent_action, my_action):
    points = 0
    # Points for outcome
    if my_action == 'X':
        points += 0
    elif my_action == 'Y':
        points += 3
    elif my_action == 'Z':
        points += 6
    
    # Points for chosen action
    if opponent_action == 'A':
        if my_action == 'X':
            points += 3
        elif my_action == 'Y':
            points += 1
        elif my_action == 'Z':
            points += 2
    elif opponent_action == 'B':
        if my_action == 'X':
            points += 1
        elif my_action == 'Y':
            points += 2
        elif my_action == 'Z':
            points += 3
    elif opponent_action == 'C':
        if my_action == 'X':
            points += 2
        elif my_action == 'Y':
            points += 3
        elif my_action == 'Z':
            points += 1
    return points


total_points = 0
for line in lines:
    opponent_action, my_action = line.split()
    total_points += points2(opponent_action, my_action)
print('Total points: ' + str(total_points))
