import urllib.request
import os
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

with open('scraped_home.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all images, svg, icons
img_urls = set()
for m in re.findall(r'src=["\']([^"\']+\.(?:png|jpg|jpeg|webp|avif|svg|gif|ico))["\']', html):
    img_urls.add(m)

for m in re.findall(r'href=["\']([^"\']+\.(?:png|jpg|jpeg|webp|avif|svg|gif|ico))["\']', html):
    img_urls.add(m)

print(f"Found {len(img_urls)} media URLs in homepage:")
for u in sorted(img_urls):
    print(" -", u)

