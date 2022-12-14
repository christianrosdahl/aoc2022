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

# # Advent of Code 2022 - Day 14

# Load data
file = open('input.txt','r')
input_lines = file.readlines()
for i in range(len(input_lines)):
    input_lines[i] = input_lines[i].replace('\n', '')

# +
# Get endpoints of all lines representing rocks
all_line_ends = []
for input_line in input_lines:
    line_ends = []
    points = input_line.split(' -> ')
    for point in points:
        x, y = point.split(',')
        x, y = int(x), int(y)
        line_ends.append((x,y))
    all_line_ends.append(line_ends)

# Get all points blocked by rocks
rock_points = set()
for line_ends in all_line_ends:
    for i in range(len(line_ends)-1):
        x1, y1 = line_ends[i] # End point 1
        x2, y2 = line_ends[i+1] # End point 2
        if y2 - y1 == 0: # Horizontal line
            y = y1
            if x2 < x1:
                x1, x2 = x2, x1
            for x in range(x1, x2+1):
                rock_points.add((x,y))
        elif x2 - x1 == 0: # Vertical line
            x = x1
            if y2 < y1:
                y1, y2 = y2, y1
            for y in range(y1, y2+1):
                rock_points.add((x,y))
# -

source = (500,0) # Location of sand source
lowest_point = max([y for (x,y) in rock_points]) # Lowest point with rocks


def blocked(pos, rock_points, sand_points, floor_y=float('inf')):
    # Check if pos is a blocked position, by rocks, sand or a potential floor
    # Returns: True if pos is not blocked
    return pos in rock_points or pos in sand_points or pos[1] >= floor_y


# ## Part 1

# Get all points containing sand
sand_points = set()
overflow = False # True when sand flows into the abyss
while not overflow:
    pos = source # Position of currently falling sand unit
    can_move = True # Sand unit can move further
    while pos[1] < lowest_point and can_move:
        if not blocked((pos[0], pos[1]+1), rock_points, sand_points):
            pos = (pos[0], pos[1]+1)
        elif not blocked((pos[0]-1, pos[1]+1), rock_points, sand_points):
            pos = (pos[0]-1, pos[1]+1)
        elif not blocked((pos[0]+1, pos[1]+1), rock_points, sand_points):
            pos = (pos[0]+1, pos[1]+1)
        else:
            can_move = False
        if pos[1] >= lowest_point:
            overflow = True
    if not overflow:
        sand_points.add(pos)

print('Number of sand units that come to rest: ' + str(len(sand_points)))

# ## Part 2

floor_y = lowest_point + 2 # Add floor under rocks

# Get all points containing sand
sand_points = set()
sand_units = 0
overflow = False
while not overflow:
    pos = source
    can_move = True
    while can_move:
        if not blocked((pos[0], pos[1]+1), rock_points, sand_points, floor_y):
            pos = (pos[0], pos[1]+1)
        elif not blocked((pos[0]-1, pos[1]+1), rock_points, sand_points, floor_y):
            pos = (pos[0]-1, pos[1]+1)
        elif not blocked((pos[0]+1, pos[1]+1), rock_points, sand_points, floor_y):
            pos = (pos[0]+1, pos[1]+1)
        else:
            can_move = False
    if pos == source:
        overflow = True
    sand_points.add(pos)

print('Number of sand units that come to rest: ' + str(len(sand_points)))
