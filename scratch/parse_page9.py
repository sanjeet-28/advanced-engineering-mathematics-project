import fitz

def parse_columns(page_idx):
    doc = fitz.open(r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\ch11.pdf")
    page = doc[page_idx]
    blocks = page.get_text("blocks")
    
    left_col = []
    right_col = []
    
    for b in blocks:
        # b = (x0, y0, x1, y1, text, block_no, block_type)
        x0, y0, x1, y1, text, block_no, block_type = b
        
        # If it's a page header or footer, skip or print separately
        if y0 < 50 or y1 > 750:
            print(f"Header/Footer Block ({x0:.1f}, {y0:.1f}): {repr(text)}")
            continue
            
        if x0 < 280:
            left_col.append(b)
        else:
            right_col.append(b)
            
    # Sort columns by y-coordinate
    left_col.sort(key=lambda x: x[1])
    right_col.sort(key=lambda x: x[1])
    
    print("\n--- LEFT COLUMN ---")
    for b in left_col:
        print(f"[{b[1]:.1f}]: {repr(b[4])}")
        
    print("\n--- RIGHT COLUMN ---")
    for b in right_col:
        print(f"[{b[1]:.1f}]: {repr(b[4])}")
        
    doc.close()

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    parse_columns(8) # page 9 is index 8
