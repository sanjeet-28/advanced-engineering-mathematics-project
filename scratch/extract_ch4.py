import pypdf

def extract_all_pages(pdf_path, txt_path):
    reader = pypdf.PdfReader(pdf_path)
    print(f"Reading {pdf_path}...")
    full_text = []
    for i, page in enumerate(reader.pages):
        page_text = page.extract_text()
        full_text.append(f"=== PAGE {i+1} ===")
        full_text.append(page_text)
    
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(full_text))
    print(f"Successfully wrote raw text of {len(reader.pages)} pages to {txt_path}")

if __name__ == "__main__":
    extract_all_pages(
        r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\ch4.pdf",
        r"C:\Users\sanje\.gemini\antigravity-ide\brain\9b994fc8-50cc-41e7-bea6-9f520c2c767c\scratch\ch4_text_raw.txt"
    )
