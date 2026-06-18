import pypdf

reader = pypdf.PdfReader(r"c:\Users\govin\OneDrive\Desktop\bhandari 2\advanced-engineering-mathematics-project\ch16 of admathsbook.pdf")
print("Total pages:", len(reader.pages))
for idx, page in enumerate(reader.pages):
    images = page.images
    if len(images) > 0:
        print(f"Page {idx+1} has {len(images)} images: {[img.name for img in images]}")
