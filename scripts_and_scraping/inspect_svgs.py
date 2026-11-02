import re
from bs4 import BeautifulSoup

for page in ['rendered_home.html', 'scraped_pages/how-it-works.html', 'scraped_pages/faq.html', 'scraped_pages/contact.html']:
    with open(page, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    svgs = soup.find_all('svg')
    print(f"\n{page}: {len(svgs)} svgs found")
    for s in svgs[:5]:
        cls = s.get('class', '')
        viewBox = s.get('viewbox') or s.get('viewBox')
        print(f"  class={cls} viewBox={viewBox} tag_count={len(s.find_all())}")

