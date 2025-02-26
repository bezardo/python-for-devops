import re

text = "Order 123, Invoice 9876, Code 42"
pattern = r"\d+"

matches = re.findall(pattern, text)  # ✅ Finds ALL numbers

if matches:
    print("Numbers found:", matches)  # ✅ No .group() needed
else:
    print("Nope")

op : 

Numbers found: ['123', '9876', '42']

"""
re.search() or re.match() return a single match object, so .group() works.
re.findall() returns a list, so we can just print the list directly.
"""
