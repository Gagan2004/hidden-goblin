from bs4 import BeautifulSoup
from html_to_jsx_helper import html_to_jsx

with open('scripts_and_scraping/scraped_pages/index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

main = soup.find('main')
jsx_body = html_to_jsx(str(main))

template = f"""import React from 'react';

export default function HomePage({{ navigate, onWatchVideo }}) {{
  return (
    {jsx_body}
  );
}}
"""

with open('src/pages/HomePage.jsx', 'w', encoding='utf-8') as f:
    f.write(template)

print("Generated exact HomePage.jsx successfully!")

