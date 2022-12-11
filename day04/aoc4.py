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

# # Advent of Code 2022 - Day 4

# Load data
file = open('input4.txt','r')
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')


def full_overlap(range1, range2):
    start1, end1 = range1.split('-')
    start2, end2 = range2.split('-')
    start1, end1 = int(start1), int(end1)
    start2, end2 = int(start2), int(end2)
    if start1 >= start2 and end1 <= end2:
        return True
    elif start2 >= start1 and end2 <= end1:
        return True
    else:
        return False


num_full_overlaps = 0
for line in lines:
    range1, range2 = line.split(',')
    if full_overlap(range1, range2):
        num_full_overlaps += 1
print('Number of full overlaps: ' + str(num_full_overlaps))


def partial_overlap(range1, range2):
    start1, end1 = range1.split('-')
    start2, end2 = range2.split('-')
    start1, end1 = int(start1), int(end1)
    start2, end2 = int(start2), int(end2)
    if end1 < start2 or end2 < start1:
        return False
    else:
        return True


num_partial_overlaps = 0
for line in lines:
    range1, range2 = line.split(',')
    if partial_overlap(range1, range2):
        num_partial_overlaps += 1
print('Number of partial overlaps: ' + str(num_partial_overlaps))
