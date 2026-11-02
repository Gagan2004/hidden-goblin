import re

with open('all_styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the broken relative @font-face rules that look for ../media/*.woff2
clean_css = re.sub(r'@font-face\s*\{[^}]*format\(["\']woff2["\']\)[^}]*\}', '', css)

# Make sure paw cursor paths point to /cursor/paw.svg
clean_css = clean_css.replace('url(/cursor/paw.svg)', 'url("/cursor/paw.svg")')
clean_css = clean_css.replace('url(/cursor/paw-press.svg)', 'url("/cursor/paw-press.svg")')

header = """@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --color-cocoa: #2a170e;
  --color-cocoa-soft: #5a3a28;
  --color-milk: #fffdf8;
  --color-honey: #f2be6b;
  --color-honey-soft: #fbe3b4;
  --color-toffee: #c2622b;
  --color-toffee-deep: #a24a1a;
  --color-toffee-ink: #8e3f15;
  --color-sky: #bfddf5;
  --color-sky-deep: #2f6e9e;
  --color-blush: #f9cdbf;
  --gutter: clamp(1rem, 4vw, 3.5rem);
  --header-h: 4.75rem;
  --bar-h: 0px;
}

@media (max-width: 768px) {
  :root {
    --header-h: 4rem;
    --bar-h: calc(4rem + env(safe-area-inset-bottom));
  }
}

.font-plush {
  font-family: 'Fraunces', Georgia, serif;
}
.font-sans {
  font-family: 'Figtree', system-ui, sans-serif;
}
.font-scrawl, .font-hand {
  font-family: 'Shantell Sans', cursive;
}

body {
  font-family: 'Figtree', system-ui, sans-serif;
  background-color: var(--color-milk);
  color: var(--color-cocoa);
  margin: 0;
  padding: 0;
  -webkit-font-smoothing: antialiased;
}

"""

with open('src/index.css', 'w', encoding='utf-8') as f:
    f.write(header + clean_css)

print("Created src/index.css successfully!")

