import re

names = ['Finn   Bindeballe',
        'Geir Anders Berge',
        'HappyCodingRobot',
        'Ron       Cromberge',
        'Sohil'
        ]

# Find people with first and last name only
regex = r'^\w+\s+\w+$'

for name in names:
    result = re.search(regex, name)
    if result:
        print(name)

