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

# # Advent of Code 2022 - Day 3

# Load data
file = open('input.txt','r')
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')


def get_common_item(compartment1, compartment2):
    for item in compartment1:
        if item in compartment2:
            return item


common_items = []
for line in lines:
    compartment1 = line[:int(round(len(line)/2))]
    compartment2 = line[int(round(len(line)/2)):]
    common_item = get_common_item(compartment1, compartment2)
    common_items.append(common_item)

all_items = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priority_values = list(range(1,53))
priority = {}
for i in range(len(all_items)):
    priority[all_items[i]] = priority_values[i]
print('Priorities: ')
print(priority)

priorities_sum = 0
for item in common_items:
    priorities_sum += priority[item]
print('Sum of priorities for common items:')
print(priorities_sum)

groups = []
for first_in_group in range(0,len(lines),3):
    group = []
    group.append(lines[first_in_group])
    group.append(lines[first_in_group + 1])
    group.append(lines[first_in_group + 2])
    groups.append(group)
print(groups[:3])


def get_common_item2(elf1, elf2, elf3):
    for item in elf1:
        if item in elf2 and item in elf3:
            return item


common_items = []
for group in groups:
    common_items.append(get_common_item2(group[0], group[1], group[2]))
print(common_items)

priorities_sum = 0
for item in common_items:
    priorities_sum += priority[item]
print('Sum of priorities for common items:')
print(priorities_sum)
