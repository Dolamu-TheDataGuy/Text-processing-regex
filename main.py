import re

# dates = """
# 01.04.2020
# 2020.04.01
# 2020.04.01
# 2020-05-23
# 2020-06-11
# 2020-07-10
# 2020-08-13 
# """


my_string = """
hello world
1223
2020-05-20
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T
researcher@gmail.com
python-researcher@gmx.de
pythonscientist123@my-domain.org
"""
pattern = re.compile(r"[a-zA-Z0-9-]+\@\w+[.-]?\w+\.(com|org|de)") # r - means raw string
matches = pattern.finditer(my_string)


# match(), search(), findall(), finditer()
# split, sub
# for match in matches:
#     print(match)

# group, start, end, span
for match in matches:
    print(match.group())

# split
testing_string = "123abc456789abc123ABC"
pattern = re.compile(r"abc")
splitted = pattern.split(testing_string)
print(splitted)


# sub
test_beat = "hello world, you are the best of both world"
pattern = re.compile(r"world")
subbed_string = pattern.sub("planet", test_beat)
print(subbed_string)


urls = """
hello
2020-05-20
http://python-engineer.com
https://www.python-engineer.com
http://www.pyeng.net
"""

pattern = re.compile(r"http(s)?\://(www\.)?[a-zA-Z0-9-+]+\.(com|net)")
matches = pattern.finditer(urls)

for match in matches:
    print(match.group())
