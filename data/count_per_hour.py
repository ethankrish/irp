#!/usr/bin/env python

from datetime import datetime, timedelta
from collections import defaultdict

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
    while key <= keys[-1]:
        print key,"|",counts[key]
        key = key + timedelta(hours=1)


