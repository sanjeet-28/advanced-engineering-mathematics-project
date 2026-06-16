import fitz

doc = fitz.open(r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\ch4.pdf")
print("Total pages:", len(doc))
for i in range(2):
    print(f"=== PAGE {i+1} ===")
    print(doc[i].get_text())
