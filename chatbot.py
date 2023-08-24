import re


content = """
order #56474849303
order #56475647483
order#574748494904
"""

pattern = re.compile(r"(order)\s\#[0-9]+")
matches = pattern.finditer(content)

for match in matches:
    print(match.group())