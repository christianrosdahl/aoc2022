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

# # Advent of Code 2022 - Day 9

# ## Part 1

# Load data
file = open('input9.txt','r')
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')


def touching(head, tail):
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        return True
    else:
        return False


def get_change_from_direction(direction):
    if direction == 'U':
        return (0,1)
    elif direction == 'D':
        return (0,-1)
    elif direction == 'L':
        return (-1,0)
    elif direction == 'R':
        return (1,0)


def get_change_when_not_touching(head, tail):
    if head[0] - tail[0] == 0: # Same row - move tail 1 step towards head
        return (0, int((head[1] - tail[1]) / abs(head[1] - tail[1])))
    elif head[1] - tail[1] == 0: # Same column - move tail 1 step towards head
        return (int((head[0] - tail[0]) / abs(head[0] - tail[0])), 0)
    else: # Diagonal difference - move tail one step along diagonal towards head
        return (int((head[0] - tail[0]) / abs(head[0] - tail[0])), 
               int((head[1] - tail[1]) / abs(head[1] - tail[1])))


def get_new_pos(head_old, head_new, tail_old):
    if not touching(head_new, tail_old):
        change = get_change_when_not_touching(head_new, tail_old)
        tail_new = (tail_old[0] + change[0], tail_old[1] + change[1])
    else:
        tail_new = tail_old
    return tail_new


# + tags=[]
head_pos = (0,0)
tail_pos = (0,0)
all_tail_pos = {tail_pos}
for line in lines:
    direction, num_steps = line.split()
    num_steps = int(num_steps)
    for step in range(num_steps):
        change = get_change_from_direction(direction)
        head_pos_new = (head_pos[0] + change[0], head_pos[1] + change[1])
        tail_pos_new = get_new_pos(head_pos, head_pos_new, tail_pos)
        all_tail_pos.add(tail_pos_new)
        head_pos = head_pos_new
        tail_pos = tail_pos_new
# -

print('Number of positions that the tail has visited: ' + str(len(all_tail_pos)))


# ## Part 2

def get_new_positions(knot_positions, change):
    new_knot_positions = []
    head_pos = knot_positions[0]
    head_pos_new = (head_pos[0] + change[0], head_pos[1] + change[1])
    new_knot_positions.append(head_pos_new)
    for i in range(0, len(knot_positions)-1):
        head_pos = knot_positions[i]
        tail_pos = knot_positions[i+1]
        tail_pos_new = get_new_pos(head_pos, head_pos_new, tail_pos)
        new_knot_positions.append(tail_pos_new)
        head_pos_new = tail_pos_new
    return new_knot_positions


# + tags=[]
knot_positions = [(0,0) for _ in range(10)]
all_tail_pos = {(0,0)}
for line in lines:
    direction, num_steps = line.split()
    num_steps = int(num_steps)
    for step in range(num_steps):
        change = get_change_from_direction(direction)
        knot_positions = get_new_positions(knot_positions, change)
        all_tail_pos.add(knot_positions[-1])
# -

print('Number of positions that the tail has visited: ' + str(len(all_tail_pos)))
