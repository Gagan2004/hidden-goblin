import urllib.request
import os

os.makedirs('scraped_puppies', exist_ok=True)
slugs = ['maltipoo-max-male', 'korean-teacup-maltipoo-female', 'copper-male']
headers = {'User-Agent': 'Mozilla/5.0'}

for s in slugs:
    url = f'https://puppy.instabizweb.com/puppies/{s}'
    filepath = f'scraped_puppies/{s}.html'
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8', errors='ignore')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Downloaded {s} ({len(content)} bytes)")

