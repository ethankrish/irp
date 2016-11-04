#!/usr/bin/env python

if __name__=="__main__":
    with open("kitchen.txt") as f:
        for line in f:
            line=line.strip()
            if line.endswith("03"):
                pass
            else:
                print(line)

