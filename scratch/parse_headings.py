import re

with open(r"C:\Users\sanje\.gemini\antigravity-ide\brain\9b994fc8-50cc-41e7-bea6-9f520c2c767c\scratch\ch4_text_raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

pages = text.split("=== PAGE ")
for i, page in enumerate(pages[1:], 1):
    lines = page.split("\n")
    for line in lines:
        if re.search(r"^\s*(4\.\d+|CHAPTER|PROBLEM SET|SUMMARY)", line, re.IGNORECASE) or "For Reference" in line:
            print(f"Page {i}: {line.strip()}")
