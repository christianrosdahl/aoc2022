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

# # Advent of Code 2022 - Day 5

# ## Part 1

# Load initial stack data
file = open('input5a.txt','r')
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

# +
# Create initial stacks
stack_width = 4
max_height = 8
num_stacks = 9
stacks = {}
for stack_num in range(1, num_stacks+1):
    stacks[stack_num] = []

for line in lines:
    pos = 0
    for stack_num in range(1, num_stacks+1):
        item = line[pos:pos+stack_width]
        if '[' in item:
            stacks[stack_num].append(item[1])
        pos += stack_width
print('Stacks: ')
print(stacks)
# -

# Load moving instructions
file = open('input5b.txt','r')
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')


def move(stacks, num_to_move, origin, dest):
    for i in range(num_to_move):
        item = stacks[origin].pop(0)
        stacks[dest].insert(0, item)


for line in lines:
    _, num_to_move, _, origin, _, dest = line.split(' ')
    num_to_move, origin, dest = int(num_to_move), int(origin), int(dest)
    move(stacks, num_to_move, origin, dest)

# +
print('Stacks: ')
print(stacks)

solution = ''
for stack_num in range(1, num_stacks+1):
    solution += stacks[stack_num][0]
print('Solution: ')
print(solution)
# -

# ## Part 2

# Load initial stack data
file = open('input5a.txt','r')
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

# +
# Create initial stacks
stack_width = 4
max_height = 8
num_stacks = 9
stacks = {}
for stack_num in range(1, num_stacks+1):
    stacks[stack_num] = []

for line in lines:
    pos = 0
    for stack_num in range(1, num_stacks+1):
        item = line[pos:pos+stack_width]
        if '[' in item:
            stacks[stack_num].append(item[1])
        pos += stack_width
print('Stacks: ')
print(stacks)
# -

# Load moving instructions
file = open('input5b.txt','r')
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')


def move2(stacks, num_to_move, origin, dest):
    items = []
    for i in range(num_to_move):
        item = stacks[origin].pop(0)
        items.append(item)
    stacks[dest] = items + stacks[dest]


for line in lines:
    _, num_to_move, _, origin, _, dest = line.split(' ')
    num_to_move, origin, dest = int(num_to_move), int(origin), int(dest)
    move2(stacks, num_to_move, origin, dest)

# +
print('Stacks: ')
print(stacks)

solution = ''
for stack_num in range(1, num_stacks+1):
    solution += stacks[stack_num][0]
print('Solution: ')
print(solution)
# -


