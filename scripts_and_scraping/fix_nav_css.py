with open('src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

rule = """
@media (max-width: 767px) {
  .tp-header__nav,
  nav[aria-label="Main"],
  header nav {
    display: none !important;
  }
}
"""

css = rule + '\n' + css
with open('src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Rule added to src/index.css successfully!")

