import fitz
import os
import re

# Paths
pdf_path = r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\ch11.pdf"
output_qmd = r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\chapters\ch11.qmd"
images_dir = r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\images"

# Ensure images directory exists
os.makedirs(images_dir, exist_ok=True)

# Helper to sanitize filenames
def sanitize_name(name):
    return re.sub(r"[^a-zA-Z0-9_-]", "_", name)

# Open PDF
doc = fitz.open(pdf_path)

# Counters for figure naming
fig_counter = 1
image_refs = []

# Collect all page texts
all_text = []
for page_number in range(len(doc)):
    page = doc[page_number]
    text = page.get_text("text")
    # Insert a placeholder for each image found on this page
    img_list = page.get_images(full=True)
    for img in img_list:
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        ext = base_image["ext"]
        fig_name = f"fig-{fig_counter:02d}.{ext}"
        fig_path = os.path.join(images_dir, fig_name)
        with open(fig_path, "wb") as img_file:
            img_file.write(image_bytes)
        # Create Quarto image reference placeholder
        img_ref = f"![]({{../images/{fig_name}}}){{#{fig_name}}}"
        image_refs.append(img_ref)
        # Insert a marker in the text where the image appears (best effort – at end of page)
        text += "\n" + img_ref + "\n"
        fig_counter += 1
    all_text.append(text)

doc.close()

# Write to QMD file
with open(output_qmd, "w", encoding="utf-8") as out_file:
    # Optional: add a generated header
    out_file.write("# Chapter 11\n\n")
    out_file.write("<!-- Auto‑generated from PDF. All original text is preserved. -->\n\n")
    for page_text in all_text:
        out_file.write(page_text)
        out_file.write("\n\n")

print(f"Extraction complete. Generated {output_qmd} with {fig_counter-1} image(s).")
