import pypdf

pdf_path = r"c:\Users\govin\OneDrive\Desktop\bhandari 2\advanced-engineering-mathematics-project\book pdfs\advanced-engineering-mathematics-10nbsped-1118049276-9781118049273_compress.pdf"
reader = pypdf.PdfReader(pdf_path)

out_path = r"c:\Users\govin\OneDrive\Desktop\bhandari 2\advanced-engineering-mathematics-project\scratch\extracted_pages.txt"

with open(out_path, "w", encoding="utf-8") as f:
    for idx in range(728, 736):
        if idx < len(reader.pages):
            f.write(f"--- INDEX {idx} ---\n")
            f.write(reader.pages[idx].extract_text())
            f.write("\n\n")

print("Extraction completed successfully!")
