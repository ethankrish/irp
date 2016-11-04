#!/usr/bin/env python

from datetime import datetime, timedelta
from collections import defaultdict
from sets import Set

counts=defaultdict(int)


if __name__=='__main__':
    with open("kitchen_clean.txt") as f:
        for line in f:
            line = line.strip()
            d = datetime.strptime(line, "%Y-%m-%d %H:%M:%S")

            dkey = datetime(d.year, d.month, d.day, d.hour)

            counts[dkey] += 1

    keys = sorted(list(counts.keys()))
    key = keys[0]

    unique_days = len(Set([k.date() for k in keys]))
    print(unique_days)

    sums = defaultdict(int)

    while key <= keys[-1]:
        key = key + timedelta(hours=1)
        sums[key.time()] = sums[key.time()] + counts[key]

    print(len(sums))

    avgs = defaultdict(int)
    keys = sorted(list(sums.keys()))
    for key in keys:
        avgs[key] = sums[key] / float(unique_days)
        print key.hour,"|", avgs[key]


