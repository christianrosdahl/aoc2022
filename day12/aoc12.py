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

# # Advent of Code 2022 - Day 12

# ## Part 1

# Load data
file = open('input12.txt','r')
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

# Create height matrix
heights = [] # Matrix with heights of each position
start = None # Start position
end = None # End position
for i, line in enumerate(lines):
    row = []
    for j, letter in enumerate(line):
        if letter == 'S': # Start position with height a
            start = (i,j)
            letter = 'a'
        elif letter == 'E': # End position with height z
            end = (i,j)
            letter = 'z'
        row.append(ord(letter) - ord('a')) # Save height as a number
    heights.append(row)

# Find neighbours of each position
neighbours = {} # Neighbours for each position
for i in range(len(heights)):
    for j in range(len(heights[0])):
        neighbours_ij = []
        for diff in [(1,0), (-1,0), (0,1), (0,-1)]:
            i_n = i + diff[0]
            j_n = j + diff[1]
            neighbour_exists = (i_n >= 0 and i_n < len(heights) and j_n >= 0 and j_n < len(heights[0]))
            if neighbour_exists:
                neighbour_reachable = ((heights[i_n][j_n] - heights[i][j]) <= 1)
                if neighbour_reachable:
                    neighbours_ij.append((i_n, j_n))
        neighbours[i,j] = neighbours_ij


# Dijkstra's algorithm for finding the shortest path
def dijkstra(heights, start, end, get_all_values=False):
    inf = float('inf') # Infinity
    unvisited = [] # Unvisited positions
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            unvisited.append((i,j))
    values = {pos: inf for pos in unvisited} # Tentative values of each position
    pos = start # Current position
    values[start] = 0
    while len(unvisited) > 0: # Run while set contains unvisited positions
        for neighbour in neighbours[pos]:
            neighbour_value = values[neighbour]
            new_value = values[pos] + 1 # Path length to neighbour via pos
            if new_value < neighbour_value:
                values[neighbour] = new_value
        unvisited.remove(pos)
        unvisited_values = {pos: values[pos] for pos in unvisited}
        if len(unvisited_values) > 0:
            pos = min(unvisited_values, key=unvisited_values.get) # Get position with smallest value
        if pos == end:
            if not get_all_values:
                break
    if get_all_values:
        return values
    else:
        return values[end]


# Get shortest path using Dijkstra's algorithm
shortest_path = dijkstra(heights, start, end)
print('The shortest path is: ' + str(shortest_path))

# ## Part 2

# ### Option 1 (Very slow - don't use it!)
# Run algorithm from each start point to the end

# + tags=[]
# # Find all positions with height a
# a_positions = []
# for i in range(len(heights)):
#     for j in range(len(heights[0])):
#         if heights[i][j] == 0:
#             a_positions.append((i,j))

# # Find shortest path from each position with height a            
# shortest_paths = []
# for i, pos in enumerate(a_positions):
#     # Compute shortest path for each starting position
#     shortest_paths.append(dijkstra(heights, pos, end))
    
#     # Print progress
#     percent_done = round(100*i/len(a_positions), ndigits=1)
#     if i % 10 == 0:
#         print(str(percent_done) + '% done')

# print('The shortest path starting from height a is: ' + str(min(shortest_paths)))
# -

# ### Option 2 (Good option for saving time and energy)
# Run backwards from end and return the whole value matrix, giving shortest paths from all start points at once

# +
# Find neighbours of each position

# Go backwards!
new_start = end
new_end = start
start = new_start
end = new_end

neighbours = {} # Neighbours for each position
for i in range(len(heights)):
    for j in range(len(heights[0])):
        neighbours_ij = []
        for diff in [(1,0), (-1,0), (0,1), (0,-1)]:
            i_n = i + diff[0]
            j_n = j + diff[1]
            neighbour_exists = (i_n >= 0 and i_n < len(heights) and j_n >= 0 and j_n < len(heights[0]))
            if neighbour_exists:
                # Reachability condition changed from part 1 to reflect that we go backwards
                neighbour_reachable = ((heights[i_n][j_n] - heights[i][j]) >= -1)
                if neighbour_reachable:
                    neighbours_ij.append((i_n, j_n))
        neighbours[i,j] = neighbours_ij

# +
# Get shortest path using Dijkstra's algorithm
values = dijkstra(heights, start, end, get_all_values=True)

# Find all positions with height a
a_positions = []
for i in range(len(heights)):
    for j in range(len(heights[0])):
        if heights[i][j] == 0:
            a_positions.append((i,j))
            
# Find shortest path from each position with height a       
shortest_paths = []
for pos in a_positions:
    shortest_paths.append(values[pos])

print('The shortest path starting from height a is: ' + str(min(shortest_paths)))
