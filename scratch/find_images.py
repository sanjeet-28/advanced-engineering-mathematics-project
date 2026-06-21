import re

file_path = r"c:\Users\govin\OneDrive\Desktop\bhandari 2\advanced-engineering-mathematics-project\chapters\ch15.qmd"

with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Search for any markdown image syntax or references to fig
matches = re.findall(r"!\[.*?\]\(.*?\)|fig-\d+", content, re.IGNORECASE)
for idx, match in enumerate(matches):
    print(f"Match {idx+1}: {match}")
