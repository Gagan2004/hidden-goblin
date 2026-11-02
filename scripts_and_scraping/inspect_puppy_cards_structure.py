from bs4 import BeautifulSoup

with open('scripts_and_scraping/scraped_pages/puppies.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

sb = soup.find('section', class_='tp-sketchbook')
# Find the grid or list containing puppy cards
cards = sb.find_all(lambda tag: tag.name in ['article', 'li', 'div'] and tag.get('class') and any('pup' in c or 'card' in c for c in tag.get('class')))
print("Found card candidates:", len(cards))
for c in cards[:5]:
    print(c.name, c.get('class'), str(c)[:120])

