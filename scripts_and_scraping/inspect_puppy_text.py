import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from bs4 import BeautifulSoup

with open('scraped_puppies/maltipoo-max-male.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("All text in maltipoo-max-male.html:")
for t in soup.find_all(['h1', 'h2', 'h3', 'p', 'span', 'li', 'button', 'a']):
    text = t.text.strip().replace('\n', ' ')
    if len(text) > 3:
        cls = ' '.join(t.get('class', []))
        if 'font-plush' in cls or 'badge' in cls or 'btn' in cls or t.name in ['h1', 'h2', 'h3']:
            print(f"<{t.name} class='{cls[:30]}'>: {text[:100]}")

