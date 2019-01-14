#! python3

import re, os

for filename in os.listdir('D:\\Python\\Books\\Automate the boring stuff with python\\Chapther 9'):
    nameFile = re.findall('.+\d+\.\w+', '\n'.join(files))
    nameFile = sorted(numbered_files)
    for match in nameFile:
        print(match)
