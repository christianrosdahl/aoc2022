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

# # Advent of Code 2022 - Day 10

# ## Part 1

# Load data
file = open('input10.txt','r')
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

# +
cycles_to_check = [20, 60, 100, 140, 180, 220]
register_values_for_cycle = {}
X = 1
cycle = 1
register_values_for_cycle[1] = X
for line in lines:
    if line == 'noop':
        cycle += 1
        register_values_for_cycle[cycle] = X
    else:
        _, value = line.split()
        value = int(value)
        cycle += 1
        register_values_for_cycle[cycle] = X
        cycle += 1
        X += value
        register_values_for_cycle[cycle] = X
        
signal_strengths = []
for cycle in cycles_to_check:
    signal_strengths.append(register_values_for_cycle[cycle] * cycle)
print('Sum of signal strengths: ' + str(sum(signal_strengths)))


# -

# ## Part 2

def show(pixel_values):
    num_rows = len(pixel_values)
    for row in range(num_rows):
        string = ''
        for pixel in range(len(pixel_values[0])):
            string += str(pixel_values[row][pixel])
        print(string)


num_rows = 6
num_pixels_per_row = 40
pixel_values = [[0 for _ in range(num_pixels_per_row)] for _ in range(num_rows)]
cycle = 1
for row in range(num_rows):
    for pixel in range(num_pixels_per_row):
        if abs(pixel - register_values_for_cycle[cycle]) <= 1:
            pixel_values[row][pixel] = '#'
        else:
            pixel_values[row][pixel] = '.'
        cycle += 1

show(pixel_values)
