import fitz
pdf_path = r"c:\\Users\\sanje\\OneDrive\\Desktop\\anew\\advanced-engineering-mathematics-project\\ch11.pdf"
out_path = r"c:\\Users\\sanje\\OneDrive\\Desktop\\anew\\advanced-engineering-mathematics-project\\scratch\\ch11_full.txt"
doc = fitz.open(pdf_path)
with open(out_path, 'w', encoding='utf-8') as f:
    for page in doc:
        f.write(page.get_text())
        f.write('\n\n')
print('Done, pages:', len(doc))
