from bs4 import BeautifulSoup
import sys
sys.path.append('scripts_and_scraping')
from html_to_jsx_helper import node_to_jsx

with open('scripts_and_scraping/teddy_hero.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

svg = soup.find('svg')
svg_jsx = node_to_jsx(svg)

print('SVG JSX length:', len(svg_jsx))

# Save the SVG JSX to a helper file so PupJourney can import or embed it
with open('scripts_and_scraping/teddy_svg_jsx.txt', 'w', encoding='utf-8') as out:
    out.write(svg_jsx)

print('Saved teddy_svg_jsx.txt')

