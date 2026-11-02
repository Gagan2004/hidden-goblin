import urllib.request
import os
import json
import re
from bs4 import BeautifulSoup

PAGES = [
    '/',
    '/puppies',
    '/gone-home',
    '/happy-families',
    '/how-it-works',
    '/faq',
    '/contact',
]

BASE_URL = 'https://puppy.instabizweb.com'

os.makedirs('scraped_pages', exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for page in PAGES:
    filename = 'index.html' if page == '/' else f"{page.strip('/')}.html"
    filepath = os.path.join('scraped_pages', filename)
    url = BASE_URL + page
    print(f"Fetching {url} -> {filepath}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f" Saved {filename} ({len(content)} bytes)")
    except Exception as e:
        print(f" Error fetching {url}: {e}")

print("Done fetching main pages.")

