import fitz

def extract_page1171_blocks():
    book_path = r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\book pdfs\advanced-engineering-mathematics-10nbsped-1118049276-9781118049273_compress.pdf"
    doc = fitz.open(book_path)
    page = doc[1170] # page 1171 is index 1170
    blocks = page.get_text("blocks")
    
    with open(r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\scratch\page1171_blocks.txt", "w", encoding="utf-8") as f:
        for b in sorted(blocks, key=lambda x: (x[1], x[0])):
            f.write(f"Block ({b[0]:.1f}, {b[1]:.1f}):\n{b[4]}\n\n")
            
    doc.close()

if __name__ == "__main__":
    extract_page1171_blocks()
