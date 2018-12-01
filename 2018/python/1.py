#!/usr/bin/env python3

import sys
from itertools import accumulate, cycle

lines = sys.stdin.readlines()

log = [int(l) for l in lines]
print(sum(log))

unique = set()
dupe = next(i for i in accumulate(cycle(log)) if i in unique or unique.add(i))
print(dupe)
