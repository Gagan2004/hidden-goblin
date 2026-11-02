import re
from bs4 import BeautifulSoup
from html_to_jsx_helper import html_to_jsx

with open('live_puppies_filter_card.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Let's inspect the filter board
filter_group = soup.find('div', {'role': 'group', 'aria-label': 'Filter puppies'})
print("Found filter group:", filter_group is not None)

# Also in puppies.html, there is tp-gone-strip at the bottom!
with open('scripts_and_scraping/scraped_pages/puppies.html', 'r', encoding='utf-8') as f:
    orig_soup = BeautifulSoup(f.read(), 'html.parser')
gone_strip = orig_soup.find('section', class_='tp-gone-strip')
print("Found gone strip:", gone_strip is not None)

# Let's combine tp-sketchbook + tp-gone-strip into the exact puppies page
full_html = f"""<div class="tp-page" data-page="puppies">
{str(soup)}
{str(gone_strip) if gone_strip else ''}
</div>"""

jsx_body = html_to_jsx(full_html)

template = f"""import React, {{ useState, useMemo }} from 'react';

export default function PuppiesPage({{ navigate, onWatchVideo }}) {{
  const [where, setWhere] = useState('Everywhere');
  const [breed, setBreed] = useState('All');
  const [gender, setGender] = useState('All');

  return (
    <div className="relative pt-[var(--header-h)] outline-none" id="main" tabIndex="-1">
      {jsx_body}
    </div>
  );
}}
"""

with open('src/pages/PuppiesPage.jsx', 'w', encoding='utf-8') as f:
    f.write(template)

print("Saved exact PuppiesPage.jsx!")
