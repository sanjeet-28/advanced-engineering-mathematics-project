import fitz

def extract_precise_answers():
    book_path = r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\book pdfs\advanced-engineering-mathematics-10nbsped-1118049276-9781118049273_compress.pdf"
    doc = fitz.open(book_path)
    
    # We found PS 11.1 answers on page 1166 and 1167 (0-indexed: 1165, 1166)
    # Let's extract the exact text blocks of page 1166 and 1167
    for i in [1165, 1166]:
        page = doc[i]
        blocks = page.get_text("blocks")
        print(f"=== PAGE {i+1} ===")
        for b in sorted(blocks, key=lambda x: (x[1], x[0])):
            if "Problem Set 11.1" in b[4] or "PS 11.1" in b[4] or "11.1" in b[4] or i == 1166:
                print(f"Block ({b[0]:.1f}, {b[1]:.1f}):\n{b[4]}\n")
                
    doc.close()

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    extract_precise_answers()
