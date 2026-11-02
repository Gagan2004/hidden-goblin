import os
import glob
import json
import re
from bs4 import BeautifulSoup
from urllib.parse import unquote

puppies = []

html_files = glob.glob('scraped_puppies/*.html')
print(f"Parsing {len(html_files)} files...")

for filepath in html_files:
    slug = os.path.basename(filepath).replace('.html', '')
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Title
    title = soup.title.string.strip() if soup.title else slug

    # Find heading (Name)
    h1 = soup.find('h1')
    name = h1.text.strip() if h1 else slug.replace('-', ' ').title()

    # Find status: available or gone home
    is_gone_home = 'gone home' in html.lower() or 'admit one' in html.lower()
    status = 'gone_home' if is_gone_home else 'available'
    if 'Available' in html:
        status = 'available'

    # Find images
    images = []
    # Search for Next.js image urls or /media/ urls
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if '/media/' in src:
            # extract the actual media path
            match = re.search(r'url=([^&]+)', src)
            if match:
                clean_src = unquote(match.group(1))
            else:
                clean_src = src
            if clean_src not in images and not clean_src.endswith('logo.png'):
                images.append(clean_src)

    # Search for video
    videos = []
    for v in soup.find_all(['video', 'source']):
        src = v.get('src', '')
        if src and src not in videos:
            videos.append(src)
    # Also check regex for mp4
    for m in re.findall(r'(/media/[^"\'\s]+\.mp4)', html):
        if m not in videos:
            videos.append(m)

    # Extract metadata like breed, age, sex, origin
    meta_tags = []
    for span in soup.find_all(['span', 'p', 'div']):
        text = span.text.strip()
        if any(w in text.lower() for w in ['month', 'weeks', 'boy', 'girl', 'maltipoo', 'pomeranian', 'poodle', 'cavapoo', 'shih', 'bichon', 'pomsky', 'maltese']):
            if len(text) < 80 and text not in meta_tags and '\n' not in text:
                meta_tags.append(text)

    # Description
    desc_p = []
    for p in soup.find_all('p'):
        text = p.text.strip()
        if len(text) > 40 and not text.startswith('TeddyPups') and not 'copyright' in text.lower():
            desc_p.append(text)

    puppies.append({
        'slug': slug,
        'title': title,
        'name': name,
        'status': status,
        'has_video': len(videos) > 0,
        'video': videos[0] if videos else None,
        'images': images,
        'metadata_snippets': meta_tags[:10],
        'description': desc_p[0] if desc_p else ''
    })

print(f"Extracted data for {len(puppies)} puppies.")
with open('puppies_data.json', 'w', encoding='utf-8') as f:
    json.dump(puppies, f, indent=2, ensure_ascii=False)

print("Saved puppies_data.json")

