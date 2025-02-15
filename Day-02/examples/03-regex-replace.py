import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)


---

import re
text = "serach korone in this korone koro"
pattern= r"koron*"
replace = "fubuki"
res = re.sub(pattern,replace,text)
if res:
    print("changed to fubuchan", res)
else:
    print("nope")  

op : changed to fubuchan serach fubukie in this fubukie fubuki


