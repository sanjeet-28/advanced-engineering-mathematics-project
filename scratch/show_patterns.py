import re

with open(r"C:\Users\sanje\.gemini\antigravity-ide\brain\9b994fc8-50cc-41e7-bea6-9f520c2c767c\scratch\ch4_text_raw.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for line_num, line in enumerate(lines, 1):
    if "/H9262" in line or "/H9266" in line or "/H9280" in line:
        print(f"Line {line_num}: {line.strip()}")
