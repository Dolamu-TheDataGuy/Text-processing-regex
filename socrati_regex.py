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

