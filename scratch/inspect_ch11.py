import fitz
import re
from collections import Counter

def inspect_pdf():
    doc = fitz.open(r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\ch11.pdf")
    print(f"Total pages: {len(doc)}")
    
    # Extract some text from first few pages and check for patterns
    text_samples = []
    anomaly_counter = Counter()
    
    for i in range(min(5, len(doc))):
        page = doc[i]
        text = page.get_text("text")
        text_samples.append((i+1, text[:500]))
        # Find matches for potential font anomalies like /H11005 or strange unicode characters
        anomalies = re.findall(r'/[Hh]\d+|[\uE000-\uF8FF]', text)
        anomaly_counter.update(anomalies)
        
    print("\nFirst page text sample:")
    print(text_samples[0][1])
    
    print("\nLast page text sample:")
    last_page = len(doc) - 1
    last_text = doc[last_page].get_text("text")
    print(last_text[:1000])
    
    print("\nMost common potential font anomalies/strange characters:")
    print(anomaly_counter.most_common(20))
    
    doc.close()

if __name__ == "__main__":
    inspect_pdf()
