import re

with open(r"C:\Users\sanje\.gemini\antigravity-ide\brain\9b994fc8-50cc-41e7-bea6-9f520c2c767c\scratch\ch4_text_raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

patterns = re.findall(r"/H\d+", text)
from collections import Counter
c = Counter(patterns)
for pat, count in c.most_common():
    print(f"{pat}: {count}")
