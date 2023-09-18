import re


name = input("What is your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")



new_name = input("What is your name? ").strip()

matches = re.search(r"^(.+), *(.+)&", name)            # walrus operator :=
if matches:= re.search(r"^(.+), *(.+)&", name):
    # last = matches.groups(1)
    # first = matches.group(2)
    name = f"{first} {last}"

print(f"hello, {name}")