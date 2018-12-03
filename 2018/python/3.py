#!/usr/bin/env python3

import sys
from collections import Counter

lines = [l.strip() for l in sys.stdin.readlines()]

c = {}
for l in lines:
    n, _, p, s = l.split(' ')
    num = n[1:]
    x_start, y_start = p[:-1].split(',')
    x_cnt, y_cnt = s.split('x')

    for x in range(0, int(x_cnt)):
        for y in range(0, int(y_cnt)):
            x_pos = int(x_start) + x
            y_pos = int(y_start) + y

            pos = '{},{}'.format(x_pos, y_pos)

            i = c.get(pos, [])
            i.append(num)
            c[pos] = i


total = len([v for _, v in c.items() if len(v) > 1])
print(total)

found = None
for l in lines:
    n = l.split(' ')[0][1:]

    overlap = False
    for v in c.values():
        if n in v and len(v) > 1:
            overlap = True

    if not overlap:
        print(n)

