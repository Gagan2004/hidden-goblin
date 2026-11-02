from bs4 import BeautifulSoup
import json
import re
from urllib.parse import unquote

with open('scraped_pages/happy-families.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

polaroids = []
for p in soup.find_all(class_=lambda c: c and 'tp-polaroid' in str(c)):
    img = p.find('img')
    caption = p.find(class_=lambda c: c and ('caption' in str(c) or 'font-scrawl' in str(c)))
    cap_text = caption.text.strip() if caption else ''
    if img:
        src = img.get('src', '')
        match = re.search(r'url=([^&]+)', src)
        clean_src = unquote(match.group(1)) if match else src
        if clean_src and not clean_src.endswith('logo.png'):
            polaroids.append({
                'image': clean_src,
                'caption': cap_text
            })

# Remove exact duplicates
unique_polaroids = []
seen = set()
for item in polaroids:
    if item['image'] not in seen:
        seen.add(item['image'])
        unique_polaroids.append(item)

print(f"Extracted {len(unique_polaroids)} unique polaroids!")
with open('extracted_happy_families.json', 'w', encoding='utf-8') as f:
    json.dump(unique_polaroids, f, indent=2, ensure_ascii=False)

