import re

# Read the file
with open('chapters/ch9.qmd', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. YAML Title block
content = content.replace(
    'title: "CHAPTER 09: Vector Differential Calculus. Grad, Div, Curl"',
    'title: "Vector Differential Calculus. Grad, Div, Curl"'
)

# 2. Main Headings
headings = {
    r'^## 9\.1 Vectors in 2-Space and 3-Space \{#sec-9-1\}': 
        '## Vectors in 2-Space and 3-Space {#sec-vectors-2-space-3-space}',
    r'^## 9\.2 Inner Product \(Dot Product\)\. Orthogonality \{#sec-9-2\}': 
        '## Inner Product (Dot Product). Orthogonality {#sec-inner-product-dot-product-orthogonality}',
    r'^## 9\.3 Vector Product \(Cross Product\) \{#sec-9-3\}': 
        '## Vector Product (Cross Product) {#sec-vector-product-cross-product}',
    r'^## 9\.4 Vector and Scalar Functions and Their Fields\. Vector Calculus: Derivatives \{#sec-9-4\}': 
        '## Vector and Scalar Functions and Their Fields. Vector Calculus: Derivatives {#sec-vector-scalar-functions-fields-derivatives}',
    r'^## 9\.5 Curves\. Arc Length\. Curvature\. Torsion \{#sec-9-5\}': 
        '## Curves. Arc Length. Curvature. Torsion {#sec-curves-arc-length-curvature-torsion}',
    r'^## 9\.6 Calculus Review: Functions of Several Variables\. Optional \{#sec-9-6\}': 
        '## Calculus Review: Functions of Several Variables (Optional) {#sec-calculus-review-functions-several-variables}',
    r'^## 9\.7 Gradient of a Scalar Field\. Directional Derivative \{#sec-9-7\}': 
        '## Gradient of a Scalar Field. Directional Derivative {#sec-gradient-scalar-field-directional-derivative}',
    r'^## 9\.8 Divergence of a Vector Field \{#sec-9-8\}': 
        '## Divergence of a Vector Field {#sec-divergence-vector-field}',
    r'^## 9\.9 Curl of a Vector Field \{#sec-9-9\}': 
        '## Curl of a Vector Field {#sec-curl-vector-field}',
    r'^## Chapter 9 Review Questions and Problems \{#sec-chapter-9-review\}': 
        '## Review Questions and Problems {#sec-review-questions-problems-chapter-9}',
    r'^## Summary of Chapter 9 \{#sec-chapter-9-summary\}': 
        '## Summary {#sec-summary-chapter-9}'
}

for pattern, repl in headings.items():
    content = re.sub(pattern, repl, content, flags=re.MULTILINE)

# 3. Figure paths:
# We need to change /images/cover.png to ../images/chapter9/fig-9-XXX.png if XXX is numeric.
# If XXX is not numeric (like p37 or proj10), change to ../images/cover.png.
def replace_fig(match):
    caption = match.group(1)
    fig_id = match.group(2)
    options = match.group(3)
    if fig_id.isdigit():
        new_path = f"../images/chapter9/fig-9-{fig_id}.png"
    else:
        new_path = "../images/cover.png"
    return f"![{caption}]({new_path}){{#fig-9-{fig_id}{options}}}"

content = re.sub(r'!\[(.*?)\]\(/images/cover.png\)\{#fig-9-([a-zA-Z0-9\-]+)(.*?)\}', replace_fig, content)

# 4. Local section references:
sec_map = {
    '9.1': '@sec-vectors-2-space-3-space',
    '9.2': '@sec-inner-product-dot-product-orthogonality',
    '9.3': '@sec-vector-product-cross-product',
    '9.4': '@sec-vector-scalar-functions-fields-derivatives',
    '9.5': '@sec-curves-arc-length-curvature-torsion',
    '9.6': '@sec-calculus-review-functions-several-variables',
    '9.7': '@sec-gradient-scalar-field-directional-derivative',
    '9.8': '@sec-divergence-vector-field',
    '9.9': '@sec-curl-vector-field'
}

# Ranges first:
content = content.replace("Sections 9.1–9.3", f"{sec_map['9.1']} to {sec_map['9.3']}")
content = content.replace("Sections 9.4 and 9.5", f"{sec_map['9.4']} and {sec_map['9.5']}")
content = content.replace("Secs. 9.7–9.9", f"{sec_map['9.7']} to {sec_map['9.9']}")
content = content.replace("9.5, 9.6.", f"{sec_map['9.5']}, {sec_map['9.6']}.")

# Individual section references:
for num, label in sec_map.items():
    content = re.sub(r'(Sec\.|Section)\s+' + re.escape(num) + r'\b', label, content)

# 5. External section/chapter references:
content = re.sub(r'Sec\.\s+7\.9\b', '@sec-vector-spaces-inner-product-spaces-linear-transformations', content)
content = re.sub(r'Sec\.\s+7\.4\b', '@sec-linear-independence-rank-matrix-vector-space', content)

# Chapter 10 sections:
content = re.sub(r'Secs?\.\s+10\.([1-9])\b', r'@sec-10-\1', content)

# Problem Set references:
content = content.replace("Problem Set 9.2", "@sec-problem-set-9-2")

# Unresolvable external references:
content = content.replace("Chaps. 9 and 10", "<!-- TODO: replace Chaps. 9 and 10 with actual chapter labels -->Chaps. 9 and 10")
content = content.replace("Chaps. 7 and 8", "<!-- TODO: replace Chaps. 7 and 8 with actual chapter labels -->Chaps. 7 and 8")
content = content.replace("Chap. 7", "<!-- TODO: replace Chap. 7 with actual chapter label -->Chap. 7")
content = content.replace("Chap. 10", "<!-- TODO: replace Chap. 10 with actual chapter label -->Chap. 10")
content = content.replace("Chaps. 12 and 18", "<!-- TODO: replace Chaps. 12 and 18 with actual chapter labels -->Chaps. 12 and 18")
content = content.replace("App. A3.4", "<!-- TODO: replace App. A3.4 with actual link -->App. A3.4")
content = content.replace("App. A4", "<!-- TODO: replace App. A4 with actual link -->App. A4")
content = content.replace("App. 4", "<!-- TODO: replace App. 4 with actual link -->App. 4")
content = content.replace("App. 1", "<!-- TODO: replace App. 1 with actual link -->App. 1")
content = content.replace("App. 2", "<!-- TODO: replace App. 2 with actual link -->App. 2")

# Save the file
with open('chapters/ch9.qmd', 'w', encoding='utf-8') as f:
    f.write(content)

print("Refactoring done successfully!")
