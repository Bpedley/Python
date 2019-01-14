#! python3

import os, re

matches = {} # {number: filename}
pattern = re.compile(r'\w+(\d+).*')

for fname in os.listdir("."):
    regex = pattern.match(fname)
    if regex:
        matches[int(regex.group(1))] = fname

lowest = min(matches) if matches else 0
for i, num in enumerate(sorted(matches), lowest):
    if i != num:
        os.rename(matches[num], "spam%03d.txt" % i)
