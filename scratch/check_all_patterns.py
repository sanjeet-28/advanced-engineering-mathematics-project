import re

with open(r"C:\Users\sanje\.gemini\antigravity-ide\brain\9b994fc8-50cc-41e7-bea6-9f520c2c767c\scratch\ch4_text_raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Find all unique patterns
patterns = set(re.findall(r"/H\d+", text))

# We want to check rare or custom ones (excluding simple digit follow-ups of basic prefixes if possible, but let's look at all of them)
ignore_prefixes = ['/H11001', '/H11002', '/H11005', '/H11546']

for pat in sorted(patterns):
    # If it starts with ignore prefix and has digits, we can skip or look at it
    is_basic = False
    for pref in ignore_prefixes:
        if pat.startswith(pref) and len(pat) > len(pref):
            is_basic = True
            break
    if pat in ignore_prefixes:
        is_basic = True
        
    # We want to inspect all non-basic ones
    if not is_basic:
        # Find some occurrences
        matches = list(re.finditer(re.escape(pat), text))
        print(f"=== Pattern {pat} (count: {len(matches)}) ===")
        for match in matches[:3]:
            start = max(0, match.start() - 60)
            end = min(len(text), match.end() + 60)
            chunk = text[start:end].replace('\n', ' ')
            safe_chunk = chunk.encode('ascii', 'backslashreplace').decode('ascii')
            print(f"  Context: ...{safe_chunk}...")
