from bs4 import BeautifulSoup

with open('rendered_home.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

teddy = soup.find(class_=lambda c: c and 'tp-hero__teddy' in str(c))
if teddy:
    with open('teddy_hero.html', 'w', encoding='utf-8') as out:
        out.write(str(teddy))
    print("Saved teddy_hero.html", len(str(teddy)))

footer_basket = soup.find(class_=lambda c: c and 'tp-basket' in str(c))
if footer_basket:
    with open('footer_basket.html', 'w', encoding='utf-8') as out:
        out.write(str(footer_basket))
    print("Saved footer_basket.html", len(str(footer_basket)))

# Also curtain edge
top_edge = soup.find(class_=lambda c: c and 'tp-curtain__edge--top' in str(c))
if top_edge:
    with open('curtain_edge_top.html', 'w', encoding='utf-8') as out:
        out.write(str(top_edge))
    print("Saved curtain_edge_top.html", len(str(top_edge)))

# Header hem
hem = soup.find(class_=lambda c: c and 'tp-header__hem' in str(c))
if hem:
    with open('header_hem.html', 'w', encoding='utf-8') as out:
        out.write(str(hem))
    print("Saved header_hem.html", len(str(hem)))

