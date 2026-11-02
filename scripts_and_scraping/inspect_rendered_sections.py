import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from bs4 import BeautifulSoup

with open('rendered_home.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

sections = soup.find_all('section')
print(f"Total sections in rendered_home: {len(sections)}")

for i, sec in enumerate(sections):
    sec_class = ' '.join(sec.get('class', []))
    h = sec.find(['h1', 'h2', 'h3'])
    htext = h.text.strip().replace('\n', ' ') if h else 'No heading'
    print(f"\n--- Section {i+1}: class='{sec_class}' | heading='{htext}' ---")
    # print buttons, links, images
    links = [a.text.strip().replace('\n', ' ') for a in sec.find_all('a') if a.text.strip()]
    btns = [b.text.strip().replace('\n', ' ') for b in sec.find_all('button') if b.text.strip()]
    imgs = [img.get('src', '')[:50] for img in sec.find_all('img')]
    print("Links:", links[:5])
    print("Buttons:", btns[:5])
    print("Images count:", len(imgs))

