import time

inp = "172851-675869"

def only_increasing(l):
    a = []
    for i in range(l[0], l[1]):
        n = str(i)
        c = True
        for j in range(len(n)-1):
            if n[j] > n[j+1]:
                c = False
                break
        if c: a += [i]
    return a

def double(arr):
    a1, a2 = [], []
    for i in arr:
        n = str(i)
        doubles = False
        d = {}
        for j in range(len(n)-1):
            if n[j] == n[j+1]:
                doubles = True
                d[n[j]] = 1 if n[j] not in d else d[n[j]] + 1
        if doubles:
            a1 += [i]
        if 1 in d.values():
            a2 += [i]
    return a1, a2

start = time.time()
a1, a2 = double(only_increasing([int(i) for i in inp.split('-')]))
print('Part 1:', len(a1))
print('Part 2:', len(a2))
print('time taken:', time.time()-start)
            
