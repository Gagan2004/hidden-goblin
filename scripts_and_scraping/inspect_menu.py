import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from bs4 import BeautifulSoup

with open('scraped_home.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

header = soup.header
print("Header HTML:")
print(str(header)[:1500])

# Look for tp-menu or menu dialog
menu = soup.find(class_=lambda c: c and 'menu' in str(c))
if menu:
    print("\nMenu element:")
    print(str(menu)[:1500])
else:
    print("\nNo direct menu element in SSR HTML")

# Search for nav links
nav = soup.find('nav')
if nav:
    print("\nNav element:")
    print(str(nav)[:1500])

