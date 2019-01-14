import re

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

batRegex1 = re.compile(r'Bat(wo)?man')
mo_1 = batRegex1.search('The Adventures of Batman')
print(mo_1.group())

mo_2 = batRegex1.search('The Adventures of Batwoman')
print(mo_2.group())
