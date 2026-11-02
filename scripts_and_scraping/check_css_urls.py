import re

with open('all_styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

urls = set(re.findall(r'url\(([^)]+)\)', css))
print(f"Total url() in all_styles.css: {len(urls)}")
for u in sorted(urls):
    print(" -", u)

