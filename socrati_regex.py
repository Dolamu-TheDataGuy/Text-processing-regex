import re

names = ['Finn Bindeballe',
        'Geir Anders Berge',
        'HappyCodingRobot',
        'Ron Cromberge',
        'Sohil'
        ]

# Find people with first and last name only
regex = r'^\w+\s+\w+$'

for name in names:
    result = re.search(regex, name)
    if result:
        print(result)

# Searh for word char sequence starting with C
regex = r'C\w*'
for name in names:
    match = re.search(regex, name)
    if match:
        print(name)
        print(match.start())
        print(match.end())
        print(match.span())
        print(match.group())


casts = ['Brian Daugette',
        'Veronica Supersonica',
        'Tony Gasparovic',
        'Patrick Germann',
        'm!sha'
        ]

# Test for first name and last name in groups and giving each group a name
# regexx = '^(?P<fn>\w+)\s+(?P<ln>\w+)$'
# for cast in casts:
#     match = re.search(regexx, cast)
#     if match:
#         print(cast)
#         print(match.group('fn'))
#         print(match.group('ln'))

# Detect last name with !
regex = '^[a-zA-Z!]+$'
for cast in casts:
    if re.search(regex, cast):
        print(cast)

regex = '[a-z]+'
for cast in casts:
    match = re.finditer(regex, cast)
    for matches in match:
        print(matches)