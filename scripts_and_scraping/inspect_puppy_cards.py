import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from bs4 import BeautifulSoup
import json

with open('scraped_pages/puppies.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print('Title:', soup.title.string if soup.title else '')

cards = soup.find_all('a', href=lambda x: x and '/puppies/' in x)
print(f"Puppy cards/links found: {len(cards)}")
seen = set()
puppies_list = []
for c in cards:
    href = c['href']
    if href in seen:
        continue
    seen.add(href)
    text = c.get_text(separator=' | ').strip()
    img = c.find('img')
    img_src = img['src'] if img and img.has_attr('src') else ''
    puppies_list.append({'href': href, 'text': text, 'img': img_src})

print(f"Unique puppies found: {len(puppies_list)}")
for p in puppies_list:
    print(p['href'], '-->', p['text'].replace('\n', ' '))

with open('extracted_puppies.json', 'w', encoding='utf-8') as f:
    json.dump(puppies_list, f, indent=2, ensure_ascii=False)
