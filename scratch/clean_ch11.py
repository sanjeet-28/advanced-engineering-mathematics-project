import re, os

# Paths
project_root = r"c:/Users/sanje/OneDrive/Desktop/anew/advanced-engineering-mathematics-project"
qmd_path = os.path.join(project_root, "chapters", "ch11.qmd")
clean_path = qmd_path  # overwrite in place

def clean_line_numbers(line):
    # Remove leading 'number: ' pattern
    return re.sub(r'^\d+:\s*', '', line)

def fix_image_syntax(line):
    # Find patterns like ![]({../images/fig-01.jpeg}){#fig-01.jpeg}
    pattern = r'!\[\]\(\{([^}]+)\}\)\{#([^}]+)\}'
    def repl(m):
        src = m.group(1).strip()
        id_full = m.group(2).strip()
        # Remove extension from id
        id_base = os.path.splitext(id_full)[0]
        return f'![]({src}){{#{id_base}}}'
    return re.sub(pattern, repl, line)

def remove_control_chars(line):
    # Remove Unicode control characters like \u0002, \u0005, etc.
    return re.sub(r'[\u0000-\u001F\u007F]', '', line)

with open(qmd_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

cleaned = []
for line in lines:
    line = clean_line_numbers(line)
    line = fix_image_syntax(line)
    line = remove_control_chars(line)
    cleaned.append(line)

with open(clean_path, 'w', encoding='utf-8') as f:
    f.writelines(cleaned)

print(f"Cleaned {len(lines)} lines in {qmd_path}")
