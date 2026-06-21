import fitz
import re

def extract_headings():
    doc = fitz.open(r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\ch11.pdf")
    
    headings = []
    full_text = []
    
    for page_idx in range(len(doc)):
        page = doc[page_idx]
        text = page.get_text("text")
        
        # We append page markers
        full_text.append(f"\n\n=== PAGE {page_idx+1} (Book Page {page_idx + 474}) ===\n")
        full_text.append(text)
        
        # Scan for headings in this page
        for line in text.splitlines():
            line_str = line.strip()
            # Look for "11.1", "11.2", etc., or "SEC.", or "PROBLEM SET", or "SUMMARY"
            if re.match(r'^(?:11\.\d|SEC\.|PROBLEM SET|SUMMARY|Chapter 11 Summary|Review Questions|C H A P T E R)', line_str, re.IGNORECASE):
                headings.append((page_idx+1, page_idx+474, line_str))
                
    with open(r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\scratch\ch11_headings.txt", "w", encoding="utf-8") as f:
        for p_idx, b_idx, h in headings:
            f.write(f"Page {p_idx} (Book {b_idx}): {h}\n")
            
    with open(r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\scratch\ch11_text_raw.txt", "w", encoding="utf-8") as f:
        f.write("".join(full_text))
        
    print(f"Extracted headings: {len(headings)}")
    doc.close()

if __name__ == "__main__":
    extract_headings()
