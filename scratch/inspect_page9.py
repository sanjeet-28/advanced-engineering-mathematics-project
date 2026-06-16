import fitz

def inspect_page_blocks(page_idx):
    doc = fitz.open(r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\ch11.pdf")
    page = doc[page_idx]
    blocks = page.get_text("blocks")
    
    with open(r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\scratch\page9_blocks.txt", "w", encoding="utf-8") as f:
        f.write(f"=== Page {page_idx+1} Blocks ===\n")
        for b in sorted(blocks, key=lambda x: (x[1], x[0])):
            f.write(f"Block ({b[0]:.1f}, {b[1]:.1f}, {b[2]:.1f}, {b[3]:.1f}):\n")
            f.write(repr(b[4]) + "\n\n")
            
    doc.close()

if __name__ == "__main__":
    inspect_page_blocks(8) # page 9 is index 8
