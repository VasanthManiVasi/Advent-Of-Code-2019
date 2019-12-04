def part1(n):
    return n//3 - 2

def part2(n):
    a = n//3 - 2
    return 0 if a <= 0 else a + part2(a)

with open('day1.txt') as f:
    inputs = f.readlines()
    print('Part 1:', sum([part1(int(i)) for i in inputs]))
    print('Part 2:', sum([part2(int(i)) for i in inputs]))
