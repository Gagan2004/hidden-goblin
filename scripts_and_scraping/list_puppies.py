from bs4 import BeautifulSoup
import urllib.request
import os

url = 'https://puppy.instabizweb.com/sitemap.xml'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    content = resp.read().decode('utf-8')

soup = BeautifulSoup(content, 'xml')
urls = [loc.text for loc in soup.find_all('loc')]

puppy_urls = [u for u in urls if '/puppies/' in u]
print(f"Total puppy detail URLs: {len(puppy_urls)}")
for u in puppy_urls:
    print(u)

