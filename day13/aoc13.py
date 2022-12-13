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

# # Advent of Code 2022 - Day 13

# ## Part 1

# Load data
file = open('input.txt','r')
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

# Put all packet pairs in a list
packet_pairs = []
for i in range(0, len(lines), 3):
    packet_pairs.append((eval(lines[i]), eval(lines[i+1])))


def get_first(left, right):
    # Get first element (list or number) out of left or right
    # Returns: 'left', 'right' or 'equal'
    first = 'equal'
    for i in range(min(len(left), len(right))):
        new_left = left[i]
        new_right = right[i]
        if type(new_left) is int and type(new_right) is int:
            if new_left < new_right:
                return 'left'
            elif new_left > new_right:
                return 'right'
        else:
            if type(new_left) is int and type(new_right) is list:
                first = get_first([new_left], new_right)
            elif type(new_left) is list and type(new_right) is int:
                first = get_first(new_left, [new_right])
            else: # type(new_left) is list and type(new_right) is list
                first = get_first(new_left, new_right)
            if not first == 'equal':
                return first

    if first == 'equal':
        if len(left) < len(right):
            first = 'left'
        elif len(right) < len(left):
            first = 'right'
        else:
            first = 'equal'
    return first


def has_right_order(left, right):
    # Check if the current order (left, right) is correct
    first = get_first(left, right)
    return first == 'left' or first == 'equal'


# + tags=[]
# Find pair indices with correct order (counted from 1)
indices_with_right_order = []
for i, pair in enumerate(packet_pairs):
    left = pair[0]
    right = pair[1]
    if has_right_order(left, right):
        indices_with_right_order.append(i+1)
# -

print('The sum of the indices of correctly ordered packet pairs: ' + str(sum(indices_with_right_order)))

# ## Part 2

# Import function for sorting from comparison function
from functools import cmp_to_key


def compare(left, right):
    # Compare function
    # Returns: -1 if left < right, 1 if left > right and 0 if left = right
    if get_first(left, right) == 'left':
        return -1
    if get_first(left,right) == 'right':
        return 1
    else:
        return 0


# +
# Collect all packets in a list
all_packets = []
for pair in packet_pairs:
    all_packets.append(pair[0])
    all_packets.append(pair[1])

# Add divider packets
divider_packets = [[[2]], [[6]]]
for packet in divider_packets:
    all_packets.append(packet)

# Sort list with all packets using the compare function
sorted_packets = sorted(all_packets, key=cmp_to_key(compare))
# -

# Find decoder key
ans = 1
for packet in divider_packets:
    ans *= (sorted_packets.index(packet) + 1)
print('The decoder key is: ' + str(ans))
