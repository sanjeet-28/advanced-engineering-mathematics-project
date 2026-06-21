import fitz
import re

def find_appendix_answers():
    # Open the complete book PDF
    book_path = r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\book pdfs\advanced-engineering-mathematics-10nbsped-1118049276-9781118049273_compress.pdf"
    doc = fitz.open(book_path)
    print(f"Total pages in book: {len(doc)}")
    
    # Let's search for "Sec. 11.1" or "Problem Set 11.1" in the latter half of the book (e.g. from page 900 onwards)
    found_pages = []
    for page_idx in range(900, len(doc)):
        page = doc[page_idx]
        text = page.get_text("text")
        if "Section 11.1" in text or "Sec. 11.1" in text or "Problem Set 11.1" in text:
            # We want to make sure it's in Appendix 2 (Answers to Odd-Numbered Problems)
            if "Answers" in text or "APP" in text or "Appendix" in text or "App. 2" in text:
                found_pages.append((page_idx, page_idx + 1))
                
    print(f"Found potential answer pages: {found_pages}")
    
    # Print the content of the found pages
    for p_idx, p_num in found_pages:
        print(f"\n================ PAGE {p_num} ================")
        print(doc[p_idx].get_text("text"))
        
    doc.close()

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    find_appendix_answers()
