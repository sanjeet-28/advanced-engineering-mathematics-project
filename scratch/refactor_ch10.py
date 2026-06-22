import re

# Read the file
with open('chapters/ch10.qmd', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. YAML Title block
content = content.replace(
    'title: "CHAPTER 10: Vector Integral Calculus. Integral Theorems"',
    'title: "Vector Integral Calculus. Integral Theorems"'
)

# 2. Main Headings
headings = {
    r'^## 10\.1 Line Integrals \{#sec-10-1\}': 
        '## Line Integrals {#sec-line-integrals}',
    r'^## 10\.2 Path Independence of Line Integrals \{#sec-10-2\}': 
        '## Path Independence of Line Integrals {#sec-path-independence-line-integrals}',
    r'^## 10\.3 Calculus Review: Double Integrals\. Optional \{#sec-10-3\}': 
        '## Calculus Review: Double Integrals (Optional) {#sec-calculus-review-double-integrals}',
    r'^## 10\.4 Green\'s Theorem in the Plane \{#sec-10-4\}': 
        '## Green\'s Theorem in the Plane {#sec-greens-theorem-plane}',
    r'^## 10\.5 Surfaces for Surface Integrals \{#sec-10-5\}': 
        '## Surfaces for Surface Integrals {#sec-surfaces-surface-integrals}',
    r'^## 10\.6 Surface Integrals \{#sec-10-6\}': 
        '## Surface Integrals {#sec-surface-integrals}',
    r'^## 10\.7 Triple Integrals\. Divergence Theorem of Gauss \{#sec-10-7\}': 
        '## Triple Integrals. Divergence Theorem of Gauss {#sec-triple-integrals-divergence-theorem-gauss}',
    r'^## 10\.8 Further Applications of the Divergence Theorem \{#sec-10-8\}': 
        '## Further Applications of the Divergence Theorem {#sec-further-applications-divergence-theorem}',
    r'^## 10\.9 Stokes\'s Theorem \{#sec-10-9\}': 
        '## Stokes\'s Theorem {#sec-stokes-theorem}',
    r'^## CHAPTER 10 REVIEW QUESTIONS AND PROBLEMS \{#sec-10-review\}': 
        '## Review Questions and Problems {#sec-review-questions-problems-chapter-10}',
    r'^## SUMMARY OF CHAPTER 10 \{#sec-10-summary\}': 
        '## Summary {#sec-summary-chapter-10}'
}

for pattern, repl in headings.items():
    content = re.sub(pattern, repl, content, flags=re.MULTILINE)

# 3. Figure paths:
# Match standard figure block: ![Caption](/images/cover.png){#fig-10-xxx options}
def replace_fig(match):
    caption = match.group(1)
    fig_id = match.group(2)
    options = match.group(3)
    if fig_id.isdigit():
        new_path = f"../images/chapter10/fig-10-{fig_id}.png"
    else:
        new_path = "../images/cover.png"
    return f"![{caption}]({new_path}){{#fig-10-{fig_id}{options}}}"

content = re.sub(r'!\[(.*?)\]\(/images/cover.png\)\{#fig-10-([a-zA-Z0-9\-]+)(.*?)\}', replace_fig, content)

# 4. Local section references:
sec_map = {
    '10.1': '@sec-line-integrals',
    '10.2': '@sec-path-independence-line-integrals',
    '10.3': '@sec-calculus-review-double-integrals',
    '10.4': '@sec-greens-theorem-plane',
    '10.5': '@sec-surfaces-surface-integrals',
    '10.6': '@sec-surface-integrals',
    '10.7': '@sec-triple-integrals-divergence-theorem-gauss',
    '10.8': '@sec-further-applications-divergence-theorem',
    '10.9': '@sec-stokes-theorem'
}

# Ranges / special text:
content = content.replace("Secs. 10.1, 10.2", f"{sec_map['10.1']}, {sec_map['10.2']}")
content = content.replace("Secs. 10.1 and 10.2", f"{sec_map['10.1']} and {sec_map['10.2']}")
content = content.replace("10.3, 10.5, 10.8.", f"{sec_map['10.3']}, {sec_map['10.5']}, {sec_map['10.8']}.")

# Individual section references:
for num, label in sec_map.items():
    # Replace Sec. 10.x / Section 10.x / Secs. 10.x / Sections 10.x
    content = re.sub(r'(?:Sec\.|Section|Secs\.|Sections)\s+' + re.escape(num) + r'\b', label, content)
    # Replace old Quarto tag @sec-10-x
    content = content.replace(f'@sec-{num.replace(".", "-")}', label)

# 5. External section/chapter references:
# Map Chapter 9 section references
ch9_sec_map = {
    '9.2': '@sec-inner-product-dot-product-orthogonality',
    '9.4': '@sec-vector-scalar-functions-fields-derivatives',
    '9.5': '@sec-curves-arc-length-curvature-torsion',
    '9.6': '@sec-calculus-review-functions-several-variables',
    '9.7': '@sec-gradient-scalar-field-directional-derivative',
    '9.8': '@sec-divergence-vector-field',
    '9.9': '@sec-curl-vector-field'
}

# Ranges / special text for Chapter 9:
content = content.replace("Secs. 9.7–9.9", f"{ch9_sec_map['9.7']} to {ch9_sec_map['9.9']}")
content = content.replace("Secs. 9.5, 10.1", f"{ch9_sec_map['9.5']}, {sec_map['10.1']}")
content = content.replace("Secs. 9.7 and 9.8", f"{ch9_sec_map['9.7']} and {ch9_sec_map['9.8']}")

for num, label in ch9_sec_map.items():
    content = re.sub(r'(?:Sec\.|Section|Secs\.|Sections)\s+' + re.escape(num) + r'\b', label, content)

# 6. Unresolvable external references:
# Chapter references
content = content.replace("Chapter 9", "<!-- TODO: replace Chapter 9 with actual chapter label -->Chapter 9")
content = content.replace("Chap. 12", "<!-- TODO: replace Chap. 12 with actual chapter label -->Chap. 12")
content = content.replace("Chaps. 12 and 18", "<!-- TODO: replace Chaps. 12 and 18 with actual chapter labels -->Chaps. 12 and 18")

# Appendix references
content = content.replace("App. 1", "<!-- TODO: replace App. 1 with actual link -->App. 1")
content = content.replace("App. 2", "<!-- TODO: replace App. 2 with actual link -->App. 2")
content = content.replace("App. 3.1", "<!-- TODO: replace App. 3.1 with actual link -->App. 3.1")
content = content.replace("App. 4", "<!-- TODO: replace App. 4 with actual link -->App. 4")

# Save the file
with open('chapters/ch10.qmd', 'w', encoding='utf-8') as f:
    f.write(content)

print("Chapter 10 refactoring done successfully!")
