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

# # Advent of Code 2022 - Day 6

# ## Part 1

# Load data
file = open('input6.txt','r')
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')


def all_unique_chars(string):
    char_set = set()
    for char in string:
        char_set.add(char)
    if len(char_set) == len(string):
        return True
    else:
        return False


def len_to_marker(marker_len, string):
    for i in range(marker_len,len(string)):
        if all_unique_chars(string[i-marker_len:i]):
            return i


string = lines[0]
marker_len = 4
ans = len_to_marker(marker_len, string)
print('The length of the string before the start-of-package marker is ' + str(ans))

# ## Part 2

string = lines[0]
marker_len = 14
ans = len_to_marker(marker_len, string)
print('The length of the string before the start-of-message marker is ' + str(ans))
