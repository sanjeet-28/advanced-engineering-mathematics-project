file_path = r"c:\Users\govin\OneDrive\Desktop\bhandari 2\advanced-engineering-mathematics-project\chapters\ch15.qmd"

with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if "fig-15-03" in line:
        print(f"Line {idx+1}: {line.strip()}")
