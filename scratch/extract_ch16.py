import pypdf
import os

def extract_all_pages(pdf_path, txt_path):
    reader = pypdf.PdfReader(pdf_path)
    print(f"Reading {pdf_path}...")
    full_text = []
    for i, page in enumerate(reader.pages):
        page_text = page.extract_text()
        full_text.append(f"=== PAGE {i+1} ===")
        full_text.append(page_text)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(txt_path), exist_ok=True)
    
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(full_text))
    print(f"Successfully wrote raw text of {len(reader.pages)} pages to {txt_path}")

if __name__ == "__main__":
    pdf_path = r"c:\Users\govin\OneDrive\Desktop\bhandari 2\advanced-engineering-mathematics-project\ch16 of admathsbook.pdf"
    txt_path = r"c:\Users\govin\OneDrive\Desktop\bhandari 2\advanced-engineering-mathematics-project\scratch\ch16_text_raw.txt"
    extract_all_pages(pdf_path, txt_path)
