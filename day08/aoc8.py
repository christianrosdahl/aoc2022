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

# # Advent of Code 2022 - Day 8

# ## Part 1

# Load data
file = open('input.txt','r')
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

# Create grid
grid = []
for line in lines:
    row = []
    for i in line:
        row.append(int(i))
    grid.append(row)


def visible(grid, pos_x, pos_y, tree_height):
    grid_height = len(grid)
    grid_width = len(grid[0])
    visible_from_left = True
    visible_from_right = True
    visible_from_up = True
    visible_from_down = True
    for i in range(0, pos_x):
        if grid[pos_y][i] >= tree_height:
            visible_from_left = False
    for i in range(pos_x+1, grid_width):
        if grid[pos_y][i] >= tree_height:
            visible_from_right = False
    for i in range(0, pos_y):
        if grid[i][pos_x] >= tree_height:
            visible_from_up = False
    for i in range(pos_y+1, grid_height):
        if grid[i][pos_x] >= tree_height:
            visible_from_down = False
    if visible_from_left or visible_from_right or visible_from_down or visible_from_up:
        return True
    else:
        return False


# +
# Count number of visible trees
num_visible = 0

# Edge trees
grid_height = len(grid)
grid_width = len(grid[0])
num_visible += 2*grid_width + 2*(grid_height-2)

# Interior trees
for pos_x in range(1, grid_width-1):
    for pos_y in range(1, grid_height-1):
        num_visible += visible(grid, pos_x, pos_y, grid[pos_y][pos_x])
        
print('Number of visible trees: ' + str(num_visible))


# -

# ## Part 2

def scenic_score(grid, pos_x, pos_y, tree_height):
    grid_height = len(grid)
    grid_width = len(grid[0])
    dist_left = 0
    dist_right = 0
    dist_up = 0
    dist_down = 0
    for i in range(1, pos_x + 1):
        dist_left = i
        if grid[pos_y][pos_x - i] >= tree_height:
            break;
    for i in range(1, grid_width - pos_x):
        dist_right = i
        if grid[pos_y][pos_x + i] >= tree_height:
            break;
    for i in range(1, pos_y + 1):
        dist_up = i
        if grid[pos_y - i][pos_x] >= tree_height:
            break;
    for i in range(1, grid_height - pos_y):
        dist_down = i
        if grid[pos_y + i][pos_x] >= tree_height:
            break;
    return dist_left * dist_right * dist_up * dist_down


# Compute maximal scenic score
max_score = 0
for pos_x in range(0, grid_width):
    for pos_y in range(0, grid_height):
        score = scenic_score(grid, pos_x, pos_y, grid[pos_y][pos_x])
        if score > max_score:
            max_score = score
print('The maximal scenic score is ' + str(max_score))
