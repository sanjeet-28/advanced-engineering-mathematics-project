import fitz

doc = fitz.open(r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\ch4.pdf")

# Extract pages 37-38 specifically (0-indexed: 36-37) - Section 4.6 main content
for i in range(36, 38):
    page = doc[i]
    text = page.get_text("text")
    print(f"\n{'='*80}")
    print(f"PDF PAGE {i+1} (Book page {i + 124})")
    print(f"{'='*80}")
    print(repr(text))

doc.close()
