from bs4 import BeautifulSoup

with open('rendered_home.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

elements = soup.find_all(class_=lambda c: c and ('teddy' in str(c) or 'basket' in str(c) or 'curtain' in str(c) or 'sun' in str(c)))
print(f"Total matching elements: {len(elements)}")
for el in elements[:15]:
    print(f"<{el.name} class='{el.get('class')}'> children={len(el.find_all())}")
    if el.name in ['svg', 'img']:
        print("   src/viewBox:", el.get('src') or el.get('viewbox') or el.get('viewBox'))
    elif len(str(el)) < 250:
        print("   html:", str(el))

