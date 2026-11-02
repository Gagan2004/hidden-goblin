import re

with open('all_styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# search for :root { ... }
roots = re.findall(r':root\s*\{([^}]+)\}', css)
for r in roots:
    print(":root block:")
    for line in r.split(';'):
        if line.strip():
            print("  ", line.strip())

# Also search for --color- or --font- or --tw-
vars = set(re.findall(r'(--[a-zA-Z0-9_-]+):\s*([^;\}]+)', css))
print(f"\nTotal custom variables: {len(vars)}")
for v, val in sorted(vars):
    if any(k in v for k in ['color', 'font', 'cocoa', 'milk', 'honey', 'butter', 'caramel', 'sky', 'brand', 'header', 'bar']):
        print(f"  {v}: {val}")

