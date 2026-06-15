import pdfplumber
import os

def main():
    pdf_path = r"c:\Users\acer\Music\advanced-engineering-mathematics-project\ch10.pdf"
    txt_dir = r"c:\Users\acer\Music\advanced-engineering-mathematics-project\garbage"
    txt_path = os.path.join(txt_dir, "ch10_text.txt")
    
    if not os.path.exists(txt_dir):
        os.makedirs(txt_dir)
        
    print("Opening ch10.pdf...")
    with pdfplumber.open(pdf_path) as pdf:
        num_pages = len(pdf.pages)
        print(f"Total pages: {num_pages}")
        
        with open(txt_path, 'w', encoding='utf-8') as f:
            for idx, page in enumerate(pdf.pages, 1):
                print(f"Extracting page {idx}/{num_pages}...")
                text = page.extract_text()
                f.write(f"=== PAGE {idx} ===\n")
                if text:
                    f.write(text)
                f.write("\n\n")
                
    print(f"Text extraction finished successfully! Written to {txt_path}")

if __name__ == "__main__":
    main()
