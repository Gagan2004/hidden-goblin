import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from bs4 import BeautifulSoup

with open('scraped_pages/happy-families.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("=== HAPPY FAMILIES ===")
for p in soup.find_all(class_=lambda c: c and ('polaroid' in str(c) or 'photowall' in str(c) or 'card' in str(c))):
    print("Class:", p.get('class'))
    print("Text:", p.get_text(separator=' | ').strip()[:100])
    img = p.find('img')
    if img:
        print("Img:", img.get('src')[:80])
    print("---")

print("\nAll text in main for happy-families:")
main = soup.main
if main:
    print(main.get_text(separator='\n').strip()[:1500])

