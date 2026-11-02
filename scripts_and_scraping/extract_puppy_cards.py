import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from bs4 import BeautifulSoup
import json
import re
from urllib.parse import unquote

with open('scraped_pages/puppies.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

cards = []
seen = set()

for a in soup.find_all('a', href=lambda h: h and h.startswith('/puppies/')):
    href = a['href']
    if href in seen:
        continue
    seen.add(href)

    slug = href.split('/')[-1]
    img = a.find('img')
    img_src = ''
    if img:
        src = img.get('src', '')
        match = re.search(r'url=([^&]+)', src)
        img_src = unquote(match.group(1)) if match else src

    text = a.get_text(separator=' | ').strip().replace('\n', ' ')
    cards.append({
        'slug': slug,
        'href': href,
        'image': img_src,
        'full_text': text
    })

print(f"Total puppy cards on /puppies: {len(cards)}")
for c in cards:
    print(c['slug'], "-->", c['full_text'][:70], "| img:", c['image'][:40])

with open('extracted_puppy_cards.json', 'w', encoding='utf-8') as f:
    json.dump(cards, f, indent=2, ensure_ascii=False)

