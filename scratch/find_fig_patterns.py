import re

def main():
    txt_path = r"c:\Users\acer\Music\advanced-engineering-mathematics-project\garbage\ch10_text.txt"
    with open(txt_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Search for all occurrences of "fig" case-insensitively and print context
    matches = re.findall(r'.{0,30}fig.{0,50}', content, re.IGNORECASE)
    print(f"Total fig matches: {len(matches)}")
    for m in matches[:30]:
        print(f"Match: {m.strip()}")

if __name__ == "__main__":
    main()
