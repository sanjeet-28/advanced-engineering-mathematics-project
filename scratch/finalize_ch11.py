import fitz, os, re, glob

pdf_path = r"c:\\Users\\sanje\\OneDrive\\Desktop\\anew\\advanced-engineering-mathematics-project\\ch11.pdf"
output_qmd = r"c:\\Users\\sanje\\OneDrive\\Desktop\\anew\\advanced-engineering-mathematics-project\\chapters\\ch11.qmd"
images_dir = r"c:\\Users\\sanje\\OneDrive\\Desktop\\anew\\advanced-engineering-mathematics-project\\images"

# Ensure images directory exists
os.makedirs(images_dir, exist_ok=True)

# Extract text
doc = fitz.open(pdf_path)
text_lines = []
for page in doc:
    text = page.get_text("text")
    # Split into lines preserving order
    for line in text.splitlines():
        text_lines.append(line)

doc.close()

# Gather image files already extracted (named fig-XX.ext)
image_files = sorted(glob.glob(os.path.join(images_dir, "fig-*.?")))
# Build markdown image references
image_refs = []
for img_path in image_files:
    img_name = os.path.basename(img_path)
    # Use relative path from QMD file (../images/)
    ref = f"![]({{../images/{img_name}}}){{#{img_name}}}"
    image_refs.append(ref)

# Write QMD
with open(output_qmd, "w", encoding="utf-8") as out:
    out.write("# Chapter 11\n\n")
    out.write("<!-- Auto‑generated from PDF. All original text is preserved. -->\n\n")
    for line in text_lines:
        out.write(line + "\n")
    out.write("\n<!-- Image references -->\n")
    for ref in image_refs:
        out.write(ref + "\n")

print(f"ch11.qmd overwritten with {len(text_lines)} text lines and {len(image_refs)} images.")
