import re


content = """
order #56474849303
order #56475647483
order#574748494904
"""

pattern = re.compile(r"(order)\s\#\d+")
matches = pattern.finditer(content)

for match in matches:
    print(match.group())

chat1 = "(123)-567-8912"
chat2 = "1234558494940"

pattern1 = r"\(?\d+\)?-?\d{3}?-?\d{4}?"
matches = re.findall(pattern1, chat1)
print(matches)