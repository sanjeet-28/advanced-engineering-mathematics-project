import fitz, os, re

pdf_path = r"c:\\Users\\sanje\\OneDrive\\Desktop\\anew\\advanced-engineering-mathematics-project\\ch11.pdf"
output_qmd = r"c:\\Users\\sanje\\OneDrive\\Desktop\\anew\\advanced-engineering-mathematics-project\\chapters\\ch11.qmd"
images_dir = r"c:\\Users\\sanje\\OneDrive\\Desktop\\anew\\advanced-engineering-mathematics-project\\images"

os.makedirs(images_dir, exist_ok=True)

# Helper to sanitize filenames
def sanitize_name(name):
    return re.sub(r"[^a-zA-Z0-9_-]", "_", name)

# Start the QMD file
with open(output_qmd, "w", encoding="utf-8") as qmd:
    qmd.write("# Chapter 11\n\n")
    qmd.write("<!-- Auto‑generated from PDF. All original text and images are preserved. -->\n\n")
    doc = fitz.open(pdf_path)
    fig_counter = 1
    for page_number in range(len(doc)):
        page = doc[page_number]
        # Extract plain text preserving line breaks
        text = page.get_text("text")
        qmd.write(text)
        qmd.write("\n\n")
        # Extract images on this page
        img_list = page.get_images(full=True)
        for img in img_list:
            xref = img[0]
            base = doc.extract_image(xref)
            ext = base["ext"]
            img_bytes = base["image"]
            img_name = f"fig-{fig_counter:02d}.{ext}"
            img_path = os.path.join(images_dir, img_name)
            with open(img_path, "wb") as img_file:
                img_file.write(img_bytes)
            # Insert markdown reference right after the page text
            qmd.write(f"![]({{../images/{img_name}}}){{#{img_name}}}\n\n")
            fig_counter += 1
    qmd.write("\n<!-- End of auto‑generated chapter -->\n")
print(f"Transcription complete: {output_qmd} with {fig_counter-1} image(s)")
