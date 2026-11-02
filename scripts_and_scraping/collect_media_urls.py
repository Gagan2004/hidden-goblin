import re
import glob
import json
from urllib.parse import unquote

all_media = set()

# 1. From puppies_data.json
with open('puppies_data.json', 'r', encoding='utf-8') as f:
    puppies = json.load(f)

for p in puppies:
    for img in p.get('images', []):
        all_media.add(img)
    if p.get('video'):
        all_media.add(p['video'])

# 2. From all html files
for fpath in glob.glob('scraped_pages/*.html') + glob.glob('scraped_puppies/*.html'):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    # match /media/... and /brand/...
    for m in re.findall(r'(/media/[^"\'\s>&]+|/brand/[^"\'\s>&]+)', content):
        clean = unquote(m)
        all_media.add(clean)

print(f"Total unique media files to download: {len(all_media)}")

with open('all_media_urls.txt', 'w', encoding='utf-8') as f:
    for m in sorted(all_media):
        f.write(m + '\n')

print("Saved all_media_urls.txt")

