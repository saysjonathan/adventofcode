#!/usr/bin/env python3

import sys
from collections import Counter

lines = [l.strip() for l in sys.stdin.readlines()]

c = Counter()
for l in lines:
    lc = [v for _, v in Counter(list(l)).most_common()]
    for i in [2,3]:
        if i in lc:
            c[i] += 1

two, three = c.values()
print(two * three)

for l in lines:
    for j in lines:
        pairs = zip(l, j)

        match = []
        diff = []
        for o, t in pairs:
            if o == t:
                match.append(o)
            else:
                diff.append(o)

        if len(diff) == 1:
            print(''.join(match))

