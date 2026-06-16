import re

def main():
    txt_path = r"c:\Users\acer\Music\advanced-engineering-mathematics-project\garbage\ch10_text.txt"
    
    with open(txt_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    pages = content.split("=== PAGE ")
    
    sections = []
    figures = []
    
    for page in pages:
        if not page.strip():
            continue
        parts = page.split(" ===")
        page_num = int(parts[0])
        page_text = parts[1]
        
        lines = page_text.splitlines()
        for idx, line in enumerate(lines, 1):
            # Find sections
            if re.search(r'\b(?:SEC\.|SEC)\b', line, re.IGNORECASE) or re.search(r'\b10\.\d\b', line):
                sections.append(f"Page {page_num} (Line {idx}): {line.strip()}")
            # Find figures
            if re.search(r'\b(?:Fig\.|Figure)\b', line, re.IGNORECASE):
                figures.append(f"Page {page_num} (Line {idx}): {line.strip()}")
                
    # Write lists
    with open("scratch/ch10_sections_list.txt", 'w', encoding='utf-8') as f:
        f.write("\n".join(sections))
    with open("scratch/ch10_figures_list.txt", 'w', encoding='utf-8') as f:
        f.write("\n".join(figures))
        
    print(f"Found {len(sections)} potential sections and {len(figures)} potential figures.")

if __name__ == "__main__":
    main()
