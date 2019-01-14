import re, os

for filename in os.listdir('@py.exe D:\\Python\\Books\\Automate the boring stuff with python\\Chapter 8\\RegexSearch'):
    f = open(filename, 'r')
    content = f.read()
    searchRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?                # area code
        (\s|-|\.)?                        # separator
        (\d{3})                           # first 3 digits
        (\s|-|\.)                         # separator
        (\d{4})                           # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?
        )''', re.VERBOSE)
    matches = []
    for groups in searchRegex.findall(content):
       phoneNum = '-'.join([groups[1], groups[3], groups[5]])
       if groups[8] != '':
           phoneNum += ' x' + groups[8]
       matches.append(phoneNum)
    if len(matches) != 0:
        print(matches)
    f.close()
