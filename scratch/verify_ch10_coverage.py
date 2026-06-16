import re

def normalize(text):
    text = text.lower()
    # Replace common font ligature/cid codes that might appear in PDF extraction
    text = text.replace("(cid:5)", "-").replace("(cid:6)", "+").replace("(cid:3)", "=").replace("(cid:2)", "\\neq")
    # Extract words (only alphabetical, length >= 4)
    words = re.findall(r'\b[a-z]{4,}\b', text)
    return set(words)

def main():
    qmd_path = r"c:\Users\acer\Music\advanced-engineering-mathematics-project\chapters\ch10.qmd"
    txt_path = r"c:\Users\acer\Music\advanced-engineering-mathematics-project\garbage\ch10_text.txt"
    
    with open(qmd_path, 'r', encoding='utf-8') as f:
        qmd_content = f.read()
    
    qmd_words = normalize(qmd_content)
    print(f"Total normalized unique words in QMD: {len(qmd_words)}")
    
    with open(txt_path, 'r', encoding='utf-8') as f:
        txt_content = f.read()
        
    pages = txt_content.split("=== PAGE ")
    
    print("\n--- Word Overlap Analysis per Page ---")
    print(f"{'Page':<6} | {'Unique Words':<12} | {'Matched':<8} | {'Overlap %':<10}")
    print("-" * 45)
    
    low_overlap_pages = []
    
    for page in pages:
        if not page.strip():
            continue
        lines = page.splitlines()
        page_header = lines[0].strip()
        page_num = page_header.split(" ===")[0]
        page_text = "\n".join(lines[1:])
        
        page_words = normalize(page_text)
        if not page_words:
            print(f"{page_num:<6} | Empty page")
            continue
            
        matched = page_words.intersection(qmd_words)
        overlap_pct = (len(matched) / len(page_words)) * 100
        
        print(f"{page_num:<6} | {len(page_words):<12} | {len(matched):<8} | {overlap_pct:.1f}%")
        
        if overlap_pct < 75.0:
            low_overlap_pages.append((page_num, overlap_pct, page_words - qmd_words))
            
    if low_overlap_pages:
        print("\nWARNING: Some pages have less than 75% overlap:")
        for page_num, pct, missing in low_overlap_pages:
            print(f"Page {page_num}: {pct:.1f}% overlap")
            # Show up to 15 missing words
            missing_sample = sorted(list(missing))[:15]
            print(f"  Missing words sample: {missing_sample}")
    else:
        print("\nSUCCESS: All pages have >= 75% word overlap!")

if __name__ == '__main__':
    main()
