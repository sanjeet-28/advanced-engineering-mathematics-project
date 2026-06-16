import re

with open(r"C:\Users\sanje\.gemini\antigravity-ide\brain\9b994fc8-50cc-41e7-bea6-9f520c2c767c\scratch\ch4_text_raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

for match in re.finditer(r"PROBLEM SET", text, re.IGNORECASE):
    start = max(0, match.start() - 50)
    end = min(len(text), match.end() + 50)
    print(f"Match: {repr(text[start:end])}")
