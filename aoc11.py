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

# # Advent of Code 2022 - Day 11

def initiate():
    # Load data
    file = open('input11.txt','r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')

    # Get starting items for each monkey
    monkey_items = []
    for line in lines:
        if 'Starting items' in line:
            line = line[len('  Starting items: '):]
            line = line.split(', ')
            line = [int(i) for i in line]
            monkey_items.append(line)

    # Get operation for each monkey
    operations = []
    for line in lines:
        if 'Operation' in line:
            operation = line[len('  Operation: new = '):]
            operations.append(operation)

    # Get tests for each monkey
    tests = []
    for i, line in enumerate(lines):
        if 'Test' in line:
            number = line[len('  Test: divisible by '):]
            test = {}
            test['divider'] = int(number)
            test['if_true'] = int(lines[i+1].split()[-1])
            test['if_false'] = int(lines[i+2].split()[-1])
            tests.append(test)
    return lines, monkey_items, operations, tests


# ## Part 1

# +
lines, monkey_items, operations, tests = initiate()

num_rounds = 20
num_monkeys = len(monkey_items)
activity = [0 for _ in range(num_monkeys)]
for r in range(num_rounds):
    for monkey in range(num_monkeys):
        while len(monkey_items[monkey]) > 0:
            activity[monkey] += 1
            old = monkey_items[monkey].pop(0) # Old level
            level = eval(operations[monkey]) # Old level is input
            level = int(level/3)
            if level % tests[monkey]['divider'] == 0:
                throw_to = tests[monkey]['if_true']
            else:
                throw_to = tests[monkey]['if_false']
            monkey_items[throw_to].append(level)
print('Activity: ' + str(activity))
activity.sort(reverse=True)
monkey_business = activity[0] * activity[1]
print('Monkey business: ' + str(monkey_business))
# -

# ## Part 2

# +
lines, monkey_items, operations, tests = initiate()

num_rounds = 10000
num_monkeys = len(monkey_items)
activity = [0 for _ in range(num_monkeys)]

all_dividers_multiplied = 1
for test in tests:
    divider = test['divider']
    all_dividers_multiplied *= divider
    
for r in range(num_rounds):
    for monkey in range(num_monkeys):
        while len(monkey_items[monkey]) > 0:
            activity[monkey] += 1
            old = monkey_items[monkey].pop(0) # Old level
            old = old % all_dividers_multiplied
            level = eval(operations[monkey]) # Old level is input
            if level % tests[monkey]['divider'] == 0:
                throw_to = tests[monkey]['if_true']
            else:
                throw_to = tests[monkey]['if_false']
            monkey_items[throw_to].append(level)
print('Activity: ' + str(activity))
activity.sort(reverse=True)
monkey_business = activity[0] * activity[1]
print('Monkey business: ' + str(monkey_business))
