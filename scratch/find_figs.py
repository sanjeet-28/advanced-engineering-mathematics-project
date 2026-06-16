import re

def find_figures():
    with open(r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\scratch\ch11_text_raw.txt", "r", encoding="utf-8") as f:
        content = f.read()
        
    pages = content.split("=== PAGE ")
    
    for page in pages:
        if not page.strip():
            continue
        parts = page.split(" ===")
        page_num = int(parts[0].split()[0])
        book_page = int(parts[0].split()[-1].replace(")", ""))
        text = parts[1]
        
        # Look for lines containing Fig.
        for line in text.splitlines():
            if "Fig." in line:
                print(f"Page {page_num} (Book {book_page}): {line.strip()}")

if __name__ == "__main__":
    find_figures()
