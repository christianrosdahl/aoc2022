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

# +
file = open('input1.txt','r')
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

elves = [0]
for line in lines:
    if line == '':
        elves += [0]
    else:
        elves[-1] += int(line)
max(elves)
# -

elves.sort(reverse=True)
top3 = elves[0:3]
print('Top 3: ')
print(top3)
print('Top 3 sum: ')
print(sum(top3))


