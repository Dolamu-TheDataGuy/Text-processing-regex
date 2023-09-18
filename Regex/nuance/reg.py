import re

email = input("Please enter email address: ").strip()

if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print('Valid')
else:
    print('Invalid')