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

# + [markdown] tags=[]
# # Advent of Code 2022 - Day 7
# -

# ## Part 1

# Load data
file = open('input7.txt','r')
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

# Create a list with the file system
file_system = []
level = 0
for line in lines:
    if '$ cd' in line and not '..' in line:
        _, _, dir_name = line.split()
        file_system.append([level, 'dir', dir_name])
        level += 1
    elif '$ cd ..' in line:
        level -= 1
    if not '$' in line and not 'dir ' in line:
        file_size, _ = line.split()
        file_system.append([level, 'file', int(file_size)])


def sum_files(file_system, start_index):
    # Sum files in file system contained in folder at start_index
    file_sum = 0
    start_level = file_system[start_index][0]
    for i in range(start_index + 1, len(file_system)):
        level, entry_type, value = file_system[i]
        if level <= start_level:
            break
        elif entry_type == 'file':
            file_sum += value
    return file_sum


# Compute directory sizes
dir_sizes = []
for i, line in enumerate(file_system):
    level, entry_type, value = line
    if entry_type == 'dir':
        dir_sizes.append(sum_files(file_system, i))

# + tags=[]
print('Directory sizes: ' + str(dir_sizes))

# + tags=[]
print('File system: ')
print('(level, type, name/size)')
for i in file_system:
    print(i)
# -

# Compute sum of sizes of directories with a size under size_limit
size_limit = 100000
size_of_dirs_under_limit = 0
for dir_size in dir_sizes:
    if dir_size <= size_limit:
        size_of_dirs_under_limit += dir_size
print('Sum of sizes of directories under ' + str(size_limit) + ': ' + str(size_of_dirs_under_limit))

# ## Part 2

# Compute how much space that needs to be freed for the update
total_disk_space = 70000000
space_required = 30000000
# The largest file size corresponds to the outermost folder, i.e., the total file size
space_used = max(dir_sizes)
free_space = total_disk_space - space_used
needed_space = space_required - free_space
print('Space needed for update: ' + str(needed_space))

# Find the smallest directory to delete to free up enough space
min_diff = 1e10
size_of_dir_to_delete = 0
for dir_size in dir_sizes:
    if dir_size > needed_space:
        diff = dir_size - needed_space
        if diff < min_diff:
            min_diff = diff
            size_of_dir_to_delete = dir_size
print('The smallest directory that can be deleted to free enough space has size: ' 
      + str(size_of_dir_to_delete))
