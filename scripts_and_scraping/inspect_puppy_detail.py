import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from bs4 import BeautifulSoup

with open('scraped_puppies/maltipoo-max-male.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print('Title:', soup.title.string if soup.title else '')
main = soup.main
if main:
    print('Main headings:')
    for h in main.find_all(['h1', 'h2', 'h3', 'h4']):
        print(f" {h.name}: {h.text.strip()}")
    print('\nButtons / links in main:')
    for b in main.find_all(['button', 'a']):
        text = b.text.strip().replace('\n', ' ')
        href = b.get('href', '')
        if text:
            print(f" [{b.name}] {text[:40]} -> {href[:40]}")

