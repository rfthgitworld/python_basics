import re

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('My number is 415-555-4242. 455-545-4242')
# print(mo)
# print(mo.group())



# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print(mo)
# print(mo.group())
# print(mo.group(1))
# print(mo.group(2))
# print(mo.groups())

# areaCode, mainNumber = mo.groups()
# print(areaCode)
# print(mainNumber)



# phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is (415) 555-4242.')
# print(mo)
# print(mo.group())
# print(mo.group(1))
# print(mo.group(2))
# print(mo.groups())

# areaCode, mainNumber = mo.groups()
# print(areaCode)
# print(mainNumber)


# heroRegex = re.compile (r'Batman|Tina Fey')
# mo1 = heroRegex.search('Batman and Tina Fey')

# print(mo1)
# print(mo1.groups())
# print(mo1.group(0))

# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel')

# print(mo.groups())
# print(mo.group())
# print(mo.group(0))
# print(mo.group(1))


# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group())


# mo2 = batRegex.search('The Adventures of Batwoman')
# print(mo2.group())



# phoneNumRegex = re.compile(r'(\(\d\d\d\))? (\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is (415) 555-4242.')
# print(mo)
# print(mo.group())
# print(mo.group(1))
# print(mo.group(2))
# print(mo.groups())

# phoneNumRegex = re.compile(r'(\(\d\d\d\))? (\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 555-4242.')
# print(mo)
# print(mo.group())
# print(mo.group(1))
# print(mo.group(2))
# print(mo.groups())

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
# print(mo.group())

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
# mo1 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

# print(mo1)

# print(mo1[0])

# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
# mo2 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

# print(mo2)
# list1 = (mo2[0])
# print(list1)
# print(list1[0])


# agentNamesRegex = re.compile(r'Agent (\w)\w*')
# x = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')

# print(x)

# name = "Zophie a cat"

# print(name[7])
# print(name[0:6])

