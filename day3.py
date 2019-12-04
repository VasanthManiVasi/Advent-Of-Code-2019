import time
def parse(string, curr):
    """ Takes a string and current position as input and returns the x, y coordinates after moving and the amount of steps. """
    x, y = curr
    dir, step = string[0], int(string[1:])
    if dir in 'RL':
        x += step if dir == 'R' else -step
    else: 
        y += step if dir == 'U' else -step
    return x, y, step

def mark_points_in_set(s, x, y, curr, step, d):
    """ Adds all of the points in the path of the wire to the set and adds the amount of steps taken to reach the points to dictionary (d).
        Returns the current position after moving. """ 
    if y == curr[1]:
        sign = 1 if curr[0] < x else -1
        for i in range(1, step+1):
            x = curr[0] + i * sign
            s.add((x, y))
            d[(x, y)] = d[(x-1*sign, y)] + 1 
        return x, y
    sign = 1 if curr[1] < y else -1
    for i in range(1, step+1):
        y = curr[1] + i * sign
        s.add((x, y))
        d[(x, y)] = d[(x, y-1*sign)] + 1
    return x, y

def path(s, curr, strings, d):
    """ Parses the string, marks the points in the set and calls path recursively with the last string removed from the original string """
    if not strings:
        return s, d
    x, y, step = parse(strings.pop(0), curr)
    curr = mark_points_in_set(s, x, y, curr, step, d)
    return path(s, curr, strings, d)

def minimum1(s):
    min = 0
    for i in s:
        sum = abs(i[0]) + abs(i[1])
        if not min:
            min = sum
        elif min > sum:
            min = sum
    return min
            
def minimum2(s, d1, d2):
    min = 0
    for i in s:
        sum = d1[i] + d2[i]
        if not min:
            min = sum
        elif min > sum:
            min = sum
    return min
start = time.perf_counter()
with open('day3.txt') as f:
    inputs = [i.split(',') for i in f.read().split('\n')]
read = time.perf_counter()
print('read time:', read - start)

s1, d1 = path(set(), (0, 0), inputs[0], {(0, 0): 0})
s2, d2 = path(set(), (0, 0), inputs[1], {(0, 0): 0})
intersection = s1.intersection(s2)
print('Part 1:', minimum1(intersection))
print('Part 2:', minimum2(intersection, d1, d2))
end = time.perf_counter()
print('cal time:', end - read)
print('total time:',  end - start)
