import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from bs4 import BeautifulSoup
import json
import re
from urllib.parse import unquote

with open('scraped_pages/gone-home.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

tickets = []
seen = set()

for t in soup.find_all(class_=lambda c: c and 'tp-ticket' in str(c)):
    img = t.find('img')
    img_src = ''
    if img:
        src = img.get('src', '')
        match = re.search(r'url=([^&]+)', src)
        img_src = unquote(match.group(1)) if match else src

    name_el = t.find(class_=lambda c: c and 'tp-ticket__name' in str(c)) or t.find(['h2', 'h3', 'strong'])
    meta_el = t.find(class_=lambda c: c and 'tp-ticket__meta' in str(c))
    route_el = t.find(class_=lambda c: c and 'tp-ticket__route' in str(c))
    link_el = t.find('a', href=True)

    name = name_el.text.strip() if name_el else ''
    meta = meta_el.text.strip() if meta_el else ''
    route = route_el.text.strip().replace('\n', ' ') if route_el else 'TEDDYPUPS ------> HOME ♥'
    href = link_el['href'] if link_el else ''

    key = (name, meta, img_src)
    if name and key not in seen:
        seen.add(key)
        tickets.append({
            'name': name,
            'meta': meta,
            'route': route,
            'image': img_src,
            'href': href
        })

print(f"Extracted {len(tickets)} unique gone home tickets:")
for tk in tickets[:10]:
    print(" -", tk['name'], "|", tk['meta'], "|", tk['route'])

with open('extracted_gone_home.json', 'w', encoding='utf-8') as f:
    json.dump(tickets, f, indent=2, ensure_ascii=False)
