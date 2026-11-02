import os
from bs4 import BeautifulSoup
from html_to_jsx_helper import html_to_jsx

PAGES_TO_GENERATE = [
    ('HowItWorksPage.jsx', 'how-it-works.html', 'HowItWorksPage'),
    ('HappyFamiliesPage.jsx', 'happy-families.html', 'HappyFamiliesPage'),
    ('GoneHomePage.jsx', 'gone-home.html', 'GoneHomePage'),
    ('FaqPage.jsx', 'faq.html', 'FaqPage'),
    ('ContactPage.jsx', 'contact.html', 'ContactPage'),
]

for out_name, in_html, comp_name in PAGES_TO_GENERATE:
    in_path = os.path.join('scripts_and_scraping', 'scraped_pages', in_html)
    with open(in_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    main = soup.find('main')
    jsx_body = html_to_jsx(str(main))

    template = f"""import React from 'react';

export default function {comp_name}({{ navigate }}) {{
  return (
    {jsx_body}
  );
}}
"""
    out_path = os.path.join('src', 'pages', out_name)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(template)

    print(f"Generated exact {out_name} successfully!")


