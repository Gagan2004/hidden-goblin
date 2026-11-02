import urllib.request
import re

css_urls = [
    'https://puppy.instabizweb.com/_next/static/chunks/2gh-2btcjgkih.css',
    'https://puppy.instabizweb.com/_next/static/chunks/10jf32vdx50lp.css'
]

combined_css = ""
for url in css_urls:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8', errors='ignore')
        combined_css += content + "\n"

with open('all_styles.css', 'w', encoding='utf-8') as f:
    f.write(combined_css)

print(f"Total CSS size: {len(combined_css)} bytes")

# Extract font-family
fonts = set(re.findall(r'font-family:\s*([^;\}]+)', combined_css))
print("\nFonts detected:")
for f in fonts:
    print(" -", f.strip())

# Extract color variables
colors = set(re.findall(r'--[a-zA-Z0-9_-]*(?:color|bg|milk|cocoa|brand|sand|caramel)[a-zA-Z0-9_-]*:\s*([^;\}]+)', combined_css))
print("\nColor variables detected:")
for c in colors:
    print(" -", c.strip())

# Extract custom class names starting with tp- or btn-
custom_classes = set(re.findall(r'\.((?:tp-|btn-|badge-)[a-zA-Z0-9_-]+)', combined_css))
print(f"\nCustom classes ({len(custom_classes)}):")
for cl in sorted(custom_classes):
    print(" -", cl)

