from bs4 import BeautifulSoup

with open('scraped_puppies/maltipoo-max-male.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

body = soup.body
if body:
    print("Body children:")
    for child in body.children:
        if child.name:
            print(child.name, child.get('class'), child.get('id'))

# Let's search for "Max" or "Maltipoo"
for el in soup.find_all(text=lambda t: t and 'Max' in t):
    parent = el.parent
    print(f"Parent: <{parent.name} class='{parent.get('class')}'> text='{el.strip()[:60]}'")

