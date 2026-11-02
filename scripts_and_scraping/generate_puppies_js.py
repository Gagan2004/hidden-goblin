import json
import glob
import re
import os
from bs4 import BeautifulSoup
from urllib.parse import unquote

# Read sitemap to map slug -> image
with open('scraped_pages/index.html', 'r', encoding='utf-8') as f:
    pass

import xml.etree.ElementTree as ET
sitemap_tree = ET.parse('sitemap.xml') if os.path.exists('sitemap.xml') else None
sitemap_img_map = {}
if os.path.exists('sitemap_urls.txt'):
    pass

# We have the list from earlier:
# In sitemap:
# https://puppy.instabizweb.com/puppies/<slug>
# followed by https://puppy.instabizweb.com/media/...

# Let's read sitemap from web or file
import urllib.request
url = 'https://puppy.instabizweb.com/sitemap.xml'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        xml_content = resp.read().decode('utf-8')
    soup_xml = BeautifulSoup(xml_content, 'xml')
    urls = [loc.text for loc in soup_xml.find_all('loc')]
    curr_pup = None
    for u in urls:
        if '/puppies/' in u:
            curr_pup = u.split('/puppies/')[-1]
        elif '/media/' in u and curr_pup:
            media_rel = '/' + u.split('instabizweb.com/')[-1]
            if curr_pup not in sitemap_img_map:
                sitemap_img_map[curr_pup] = media_rel
            curr_pup = None
except Exception as e:
    print("Sitemap error:", e)

print(f"Mapped {len(sitemap_img_map)} puppy images from sitemap")

# Read extracted cards
with open('extracted_puppy_cards.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)

card_map = {c['slug']: c for c in cards}

# Read extracted gone home
with open('extracted_gone_home.json', 'r', encoding='utf-8') as f:
    gone_home_tickets = json.load(f)

puppies = []
seen_slugs = set()

# First process all scraped puppy html files
html_files = sorted(glob.glob('scraped_puppies/*.html'))
for fpath in html_files:
    slug = os.path.basename(fpath).replace('.html', '')
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Find heading (Name)
    h1 = soup.find('h1')
    name = h1.text.strip() if h1 else slug.replace('-', ' ').title()

    # Determine status
    card = card_map.get(slug)
    status = 'available'
    if card and 'gone home' in card['full_text'].lower():
        status = 'gone_home'
    elif 'gone home' in html.lower() and 'admit one' in html.lower():
        status = 'gone_home'
    elif any(slug in tk.get('href', '') for tk in gone_home_tickets):
        status = 'gone_home'

    # Breed, gender, age detection
    breed = 'Maltipoo'
    if 'pomeranian' in slug.lower() or 'pomeranian' in name.lower():
        breed = 'Pomeranian'
    elif 'cavapoo' in slug.lower():
        breed = 'Cavapoo'
    elif 'poodle' in slug.lower():
        breed = 'Poodle'
    elif 'shitzu' in slug.lower() or 'shih tzu' in name.lower() or 'shih-tzu' in slug.lower():
        breed = 'Shih Tzu'
    elif 'bichon' in slug.lower():
        breed = 'Bichon'
    elif 'pomsky' in slug.lower() or 'pomski' in slug.lower():
        breed = 'Pomsky'
    elif 'maltese' in slug.lower():
        breed = 'Maltese'
    elif 'maltipoo' in slug.lower():
        breed = 'Maltipoo'

    gender = 'boy' if ('male' in slug.lower() or 'boy' in slug.lower()) else 'girl'
    if 'male-female' in slug.lower() or 'boy & girl' in html.lower():
        gender = 'boy & girl'

    age = '2 months'
    age_match = re.search(r'(\d+(?:\.\d+)?\s*(?:months?|weeks?))', html, re.IGNORECASE)
    if card and ('month' in card['full_text'] or 'week' in card['full_text']):
        cm = re.search(r'(\d+(?:\.\d+)?\s*(?:months?|weeks?))', card['full_text'], re.IGNORECASE)
        if cm:
            age = cm.group(1)
    elif age_match:
        age = age_match.group(1)

    origin = 'Korea' if ('korean' in slug.lower() or 'teacup' in slug.lower()) else 'Local'

    # Images
    images = []
    # Primary image from sitemap or card
    primary_img = sitemap_img_map.get(slug) or (card['image'] if card else '')
    if primary_img and primary_img not in images:
        images.append(primary_img)

    for m in re.findall(r'(/media/[^"\'\s>&]+\.(?:webp|jpg|jpeg|png|avif))', html):
        clean_m = unquote(m).replace('\\', '/')
        if clean_m not in images and not clean_m.endswith('logo.png') and not 'woff2' in clean_m:
            images.append(clean_m)

    # Videos
    videos = []
    for m in re.findall(r'(/media/[^"\'\s>&]+\.mp4)', html):
        clean_v = unquote(m).replace('\\', '/')
        if clean_v not in videos:
            videos.append(clean_v)

    # Description
    desc_p = []
    for p in soup.find_all('p'):
        text = p.text.strip().replace('\n', ' ')
        if len(text) > 40 and not text.startswith('TeddyPups') and not 'copyright' in text.lower():
            desc_p.append(text)

    desc = desc_p[0] if desc_p else f"{name} is an adorable, playful, and healthy {breed} puppy with the sweetest personality. Raised with lots of love, veterinary care, and attention."

    seen_slugs.add(slug)
    puppies.append({
        'id': slug,
        'slug': slug,
        'name': name,
        'breed': breed,
        'gender': gender,
        'age': age,
        'origin': origin,
        'status': status,
        'hasVideo': len(videos) > 0 or (card and '▶ video' in card['full_text']),
        'video': videos[0] if videos else None,
        'images': images if images else ['/brand/logo.png'],
        'description': desc,
        'personality': 'Playful, affectionate, cuddly, and friendly with kids & other pets',
        'included': [
            'Official Vet Health Certificate',
            'Full Nose-to-Tail Health Check',
            'ISO Certified Microchip',
            'Vaccination Passport',
            'Deworming Complete',
            'Premium Starter Puppy Kit',
            '24/7 Breeder & Post-Adoption Support'
        ]
    })

print(f"Generated {len(puppies)} puppies!")

# Write to src/data/puppies.js
os.makedirs('src/data', exist_ok=True)
with open('src/data/puppies.js', 'w', encoding='utf-8') as f:
    f.write('export const PUPPIES = ' + json.dumps(puppies, indent=2, ensure_ascii=False) + ';\n')

print("Wrote src/data/puppies.js")

