from bs4 import BeautifulSoup

with open('scraped_puppies/maltipoo-max-male.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Check div with id S:0 or similar
for div in soup.find_all('div'):
    if div.get('id', '').startswith('S:'):
        print(f"Found streaming div id={div.get('id')}, length={len(div.text)}")
        for h in div.find_all(['h1', 'h2', 'h3']):
            print("  ", h.name, h.text.strip())

