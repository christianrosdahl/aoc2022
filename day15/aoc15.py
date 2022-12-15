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

# # Advent of Code 2022 - Day 15

# Load data
# input_name = 'input_example.txt'
input_name = 'input.txt'
file = open(input_name,'r')
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

# ## Part 1

# Get sensor and beacon positions
sensors = []
beacons = []
for line in lines:
    sensor, beacon = line.split(': ')
    x, y = sensor[len('Sensor at '):].split(', ')
    x, y = x[len('x='):], y[len('y='):]
    x, y = int(x), int(y)
    sensors.append((x,y))
    x, y = beacon[len('closest beacon is at '):].split(', ')
    x, y = x[len('x='):], y[len('y='):]
    x, y = int(x), int(y)
    beacons.append((x,y))


def distance(p1, p2):
    # Get Manhattan distance between two points p1 = (x1,y1) and p2 = (x2,y2)
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    return (abs(y2 - y1) + abs(x2 - x1))


# Get distances between sensors and nearest beacon for each sensor
distances = []
for i in range(len(sensors)):
    sensor = sensors[i]
    beacon = beacons[i]
    distances.append(distance(sensor, beacon))


def cannot_have_beacon(pos, sensors, beacons, distances):
    # Check if pos cannot have a beacon
    # Returns: True if pos cannot have a beacon
    for i in range(len(sensors)):
        if (distance(pos, sensors[i]) <= distances[i]
            and not pos in beacons):
            return True
    return False


# + tags=[]
# Find number of positions (x,y) for a given y that cannot have a beacon
if 'example' in input_name:
    y = 10
else:
    y = 2000000
max_dist = max(distances)
x_min = min([sensor[0] - max_dist for sensor in sensors])
x_max = max([sensor[0] + max_dist for sensor in sensors])
num_pos_without_beacon = 0
for x in range(x_min, x_max+1):
    if cannot_have_beacon((x,y), sensors, beacons, distances):
        num_pos_without_beacon += 1
# -

print('Number of positions (x,y) for y = ' + str(y) 
      + ' that cannot have a beacon: ' + str(num_pos_without_beacon))


# ## Part 2

def unblocked_points(intervals, limits):
    # Get all integer points between limits = (x1, x2)
    # that are not covered by any interval listed in intervals
    points = [] # All interval end points
    points.append((limits[0], 'limit'))
    points.append((limits[1], 'limit'))
    for i in intervals:
        points.append((i[0], 'start'))
        points.append((i[1], 'end'))
    points.sort(key = lambda i: i[0])
    active_intervals = 0 # Number of active intervals
    free_points = [] # Unblocked points
    for i in range(len(points)-1):
        if points[i][1] == 'start':
            active_intervals += 1
        elif points[i][1] == 'end':
            active_intervals -= 1
        if active_intervals == 0:
            free_points += list(range(points[i][0]+1, points[i+1][0]))
    return free_points


def x_potential_beacons(y, sensors, distances, x_lim):
    # Get x-values for all points (x,y) with the given y
    # within the limits x_lim = (x1,x2) that could contain beacons
    x_min, x_max = x_lim[0], x_lim[1]
    blocked_intervals = [] # Intervals that cannot contain a beacon
    for i in range(len(sensors)):
        xs, ys = sensors[i][0], sensors[i][1]
        dist = distances[i]
        dy = abs(y - ys)
        if dy <= dist:
            dx = dist - dy
            x1 = xs - dx
            x2 = xs + dx
            blocked_intervals.append([x1, x2])
    return unblocked_points(blocked_intervals, x_lim)


# Find points that could contain a beacon
x_min = 0
if 'example' in input_name:
    x_max = 20
else:
    x_max = 4000000
y_min = x_min
y_max = x_max
free_points = []
for y in range(y_min,y_max):
    unblocked_x = x_potential_beacons(y, sensors, distances, x_lim=(x_min,x_max))
    for x in unblocked_x:
        free_points.append((x, y))
print('Points that could contain a beacon: ' + str(free_points))

# Find tuning frequency
nearest_beacon = free_points[0]
x,y = nearest_beacon
tuning_freq = x*4000000 + y
print('Tuning frequency: ' + str(tuning_freq))
