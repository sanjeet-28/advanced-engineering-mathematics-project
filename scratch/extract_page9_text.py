import fitz

def extract_detailed_text(page_idx):
    doc = fitz.open(r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\ch11.pdf")
    page = doc[page_idx]
    
    # We use page.get_text("dict") to get exact details of spans
    text_dict = page.get_text("dict")
    
    with open(r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\scratch\page9_detail.txt", "w", encoding="utf-8") as f:
        for block in text_dict["blocks"]:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        f.write(f"Span at ({span['bbox'][0]:.1f}, {span['bbox'][1]:.1f}, {span['bbox'][2]:.1f}, {span['bbox'][3]:.1f}) - font: {span['font']}, size: {span['size']:.1f}\n")
                        f.write(f"  Text: {repr(span['text'])}\n\n")
                        
    doc.close()

if __name__ == "__main__":
    extract_detailed_text(8)
