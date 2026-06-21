import pypdf
import os

pdf_path = r"c:\Users\govin\OneDrive\Desktop\bhandari 2\advanced-engineering-mathematics-project\book pdfs\advanced-engineering-mathematics-10nbsped-1118049276-9781118049273_compress.pdf"

if not os.path.exists(pdf_path):
    print("PDF not found!")
    exit(1)

reader = pypdf.PdfReader(pdf_path)
print(f"Total pages: {len(reader.pages)}")

# Search for Chapter 15
for idx, page in enumerate(reader.pages):
    text = page.extract_text()
    if "CHAPTER 15" in text or "Power Series, Taylor Series" in text:
        if "705" in text or "706" in text or "707" in text:
            print(f"Found match on page index {idx} (Page number in text might be near):")
            print(text[:200])
            print("-" * 40)
