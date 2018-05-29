#!/usr/bin/env python
from __future__ import print_function
import json
import sys

with open('data/erowid.json', 'r') as handle:
    data = json.load(handle)
    N = 0
    for row in data:
        print(row['title'])
        for report in row['report']:
            print(report)
        N += 1
        if N > 100:
            sys.exit()

