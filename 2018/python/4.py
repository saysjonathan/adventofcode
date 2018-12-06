#!/usr/bin/env python3

from collections import Counter
import datetime
import re
import sys

class Log(object):
    def __init__(self, s):
        self.s = s

    @property
    def datetime(self):
        m = re.match(r"\[(\d+)\-(\d+)\-(\d+) (\d+)\:(\d+)\]", self.s)
        mi = [int(i) for i in m.groups()]
        return datetime.datetime(*mi)

    @property
    def guard(self):
        if 'Guard' in self.s:
            return self.s.split("#")[1].split(' ')[0]
        else:
            return None

    @property
    def asleep(self):
        if 'asleep' in self.s:
            return True
        else:
            return False

    @property
    def awake(self):
        if 'wake' in self.s:
            return True
        else:
            return False


lines = [Log(l.strip()) for l in sys.stdin.readlines()]
logs = sorted(lines, key=lambda x: x.datetime)

log = {}
g = None
a, w = 0, 0

for l in logs:
    if l.guard:
        g = l.guard
    elif l.asleep:
        a = l.datetime
    elif l.awake:
        w = l.datetime
        t = log.get(g, [])

        if a.minute < w.minute:
            m = list(range(a.minute, w.minute))
        else:
            ms = list(range(0, 60))
            md = list(range(w.minute, a.minute))
            m = [i for i in ms if i not in md]

        t = t + m
        log[g] = t

        a, w = 0, 0

la = {k: sum(v) for k, v in log.items()}
m = max(la, key=la.get)

c = Counter(log[m])
mc = c.most_common(1)[0][0]

print(int(m) * mc)


c = {}
for k, v in log.items():
    c[k] = Counter(v)


mc = {k: v.most_common(1)[0][1] for k, v in c.items()}
mmx = max(mc, key=mc.get)
print(int(mmx) * c[mmx].most_common(1)[0][0])

