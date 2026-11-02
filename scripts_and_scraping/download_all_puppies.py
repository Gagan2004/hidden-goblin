import urllib.request
import os
import json
from bs4 import BeautifulSoup

with open('sitemap_urls.txt', 'w') as f:
    pass

# Read sitemap
url = 'https://puppy.instabizweb.com/sitemap.xml'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    content = resp.read().decode('utf-8')

soup = BeautifulSoup(content, 'xml')
urls = [loc.text for loc in soup.find_all('loc')]

puppy_urls = [u for u in urls if '/puppies/' in u]
print(f"Total puppy detail URLs: {len(puppy_urls)}")

os.makedirs('scraped_puppies', exist_ok=True)
headers = {'User-Agent': 'Mozilla/5.0'}

for u in puppy_urls:
    slug = u.split('/puppies/')[-1]
    filepath = f'scraped_puppies/{slug}.html'
    if not os.path.exists(filepath):
        print(f"Downloading {slug}...")
        try:
            req = urllib.request.Request(u, headers=headers)
            with urllib.request.urlopen(req) as resp:
                data = resp.read().decode('utf-8', errors='ignore')
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(data)
                print(f" Saved {slug} ({len(data)} bytes)")
        except Exception as e:
            print(f" Error {slug}: {e}")
    else:
        print(f" Already have {slug}")

print("All puppy pages downloaded!")

