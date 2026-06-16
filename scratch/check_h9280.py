import re

with open(r"C:\Users\sanje\.gemini\antigravity-ide\brain\9b994fc8-50cc-41e7-bea6-9f520c2c767c\scratch\ch4_text_raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let's find occurrences of /H9280 and print their line context using backslashreplace
for match in re.finditer(r"/H9280", text):
    start = max(0, match.start() - 100)
    end = min(len(text), match.end() + 100)
    chunk = text[start:end]
    safe_chunk = chunk.encode('ascii', 'backslashreplace').decode('ascii')
    print(f"Match: ...{safe_chunk}...\n")
