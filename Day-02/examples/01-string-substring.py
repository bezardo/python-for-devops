text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")

---

text = "Python is awesome"
substring = text[text.find('is'):]  # Get "is" and everything after it
if substring in text:
 print(substring, "found in the text")
