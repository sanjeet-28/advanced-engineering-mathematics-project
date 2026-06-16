import os

def main():
    parts_dir = r"C:\Users\acer\.gemini\antigravity-ide\brain\4e301712-0e0a-42e4-a1e1-245d62d28293\scratch\ch10_parts"
    out_path = r"c:\Users\acer\Music\advanced-engineering-mathematics-project\chapters\ch10.qmd"
    
    parts = [
        "ch10_header.qmd",
        "ch10_sec1.qmd",
        "ch10_sec2.qmd",
        "ch10_sec3.qmd",
        "ch10_sec4.qmd",
        "ch10_sec5.qmd",
        "ch10_sec6.qmd",
        "ch10_sec7.qmd",
        "ch10_sec8.qmd",
        "ch10_sec9.qmd",
        "ch10_review.qmd",
        "ch10_summary.qmd"
    ]
    
    content = []
    for part in parts:
        part_path = os.path.join(parts_dir, part)
        if not os.path.exists(part_path):
            print(f"Warning: Part file {part} does not exist yet. Skipping.")
            continue
        print(f"Reading {part}...")
        with open(part_path, 'r', encoding='utf-8') as f:
            content.append(f.read())
            # Ensure there is a newline between parts
            if not content[-1].endswith('\n'):
                content[-1] += '\n'
                
    full_content = "\n".join(content)
    
    # Write to target path
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
        
    print(f"Successfully assembled {out_path} ({len(full_content)} characters)!")

if __name__ == "__main__":
    main()
