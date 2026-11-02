import re
from bs4 import BeautifulSoup
from html_to_jsx_helper import html_to_jsx

with open('scripts_and_scraping/scraped_pages/puppies.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

main = soup.find('main')
jsx_body = html_to_jsx(str(main))

template = f"""import React, {{ useState, useMemo }} from 'react';

export default function PuppiesPage({{ navigate, onWatchVideo }}) {{
  const [whereFilter, setWhereFilter] = useState('Everywhere');
  const [breedFilter, setBreedFilter] = useState('All');
  const [genderFilter, setGenderFilter] = useState('All');

  return (
    {jsx_body}
  );
}}
"""

with open('src/pages/PuppiesPage.jsx', 'w', encoding='utf-8') as f:
    f.write(template)

print("Generated exact PuppiesPage.jsx successfully!")
