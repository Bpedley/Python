import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Call me at 415-555-1011 tomorrow.')
print('Phone number found: ' + mo.group())

phoneNumRegex1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo1 = phoneNumRegex1.search('My number is 415-555-4242.')
print(mo1.group(1))
print(mo1.group(2))
print(mo1.group(0))
print(mo1.group())
print(mo1.groups())
areaCode, mainNumber = mo1.groups()
print(areaCode)
print(mainNumber)

phoneNumRegex2 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo2 = phoneNumRegex2.search('My phone number is (415) 555-4242.')
print(mo2.group(1))
print(mo2.group(2))

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo_1 = phoneRegex.search('My number is 415-555-4242')
print(mo_1.group()) #'415-555-4242'

mo_2 = phoneRegex.search('My number is 555-4242')
print(mo_2.group()) #'555-4242'
