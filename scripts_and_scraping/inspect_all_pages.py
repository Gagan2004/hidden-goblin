import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from bs4 import BeautifulSoup
import os

pages = ['index', 'puppies', 'gone-home', 'happy-families', 'how-it-works', 'faq', 'contact']

for p in pages:
    path = f'scraped_pages/{p}.html'
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    print(f"\n==================== PAGE: {p} ====================")
    print("Title:", soup.title.string if soup.title else 'No Title')
    h1s = [h.text.strip().replace('\n', ' ') for h in soup.find_all('h1')]
    h2s = [h.text.strip().replace('\n', ' ') for h in soup.find_all('h2')]
    print("H1s:", h1s)
    print("H2s:", h2s[:8])

