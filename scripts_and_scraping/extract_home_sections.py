from bs4 import BeautifulSoup

with open('scripts_and_scraping/scraped_pages/index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

main = soup.find('main')
sections = main.find_all('section')
for i, s in enumerate(sections):
    cls = s.get('class', [])
    print(f"Section {i}: {' '.join(cls)} (length: {len(str(s))})")

