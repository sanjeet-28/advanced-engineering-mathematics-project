import pypdf

pdf_path = r"c:\Users\govin\OneDrive\Desktop\bhandari 2\advanced-engineering-mathematics-project\book pdfs\advanced-engineering-mathematics-10nbsped-1118049276-9781118049273_compress.pdf"
reader = pypdf.PdfReader(pdf_path)

for idx, page in enumerate(reader.pages):
    text = page.extract_text()
    if "Proof of Theorem 1" in text and "convergent complex sequence" in text:
        print(f"Found on page index {idx}")
        print(text[:1500])
        break
