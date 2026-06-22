import re

with open('chapters/ch9.qmd', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update remaining broken references
content = content.replace("@sec-9-7", "@sec-gradient-scalar-field-directional-derivative")
content = content.replace("@sec-9-8", "@sec-divergence-vector-field")
content = content.replace("@sec-9-9", "@sec-curl-vector-field")

# 2. Insert blank lines between consecutive figures
lines = content.split('\n')
new_lines = []

def is_fig(line):
    l = line.strip()
    return l.startswith("![") and "{" in l and l.endswith("}")

for i in range(len(lines)):
    new_lines.append(lines[i])
    if is_fig(lines[i]) and i + 1 < len(lines) and is_fig(lines[i+1]):
        new_lines.append("")

content = '\n'.join(new_lines)

with open('chapters/ch9.qmd', 'w', encoding='utf-8') as f:
    f.write(content)

print("Spacing and references fixed successfully!")
