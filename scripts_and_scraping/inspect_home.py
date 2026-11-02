from bs4 import BeautifulSoup

with open('scraped_home.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print('Header:', bool(soup.header))
print('Nav:', bool(soup.nav))
print('Main:', bool(soup.main))
print('Footer:', bool(soup.footer))

sections = soup.find_all('section')
print(f'Total sections: {len(sections)}')
for i, s in enumerate(sections):
    h = s.find(['h1', 'h2', 'h3'])
    htext = h.text.strip().replace('\n', ' ') if h else 'No heading'
    sec_id = s.get('id', 'no-id')
    sec_class = ' '.join(s.get('class', []))
    print(f'Section {i+1}: id="{sec_id}" heading="{htext[:60]}" class="{sec_class[:40]}"')

