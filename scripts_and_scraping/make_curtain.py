import re
from bs4 import BeautifulSoup
import sys
sys.path.append('scripts_and_scraping')
from html_to_jsx_helper import node_to_jsx

with open('scripts_and_scraping/curtain_full.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

blanket = soup.find(class_='tp-curtain__blanket')
blanket_jsx = node_to_jsx(blanket)

output_code = """import React from 'react';

export default function PageCurtain({ state = 'idle' }) {
  return (
    <div
      aria-hidden="true"
      className="tp-curtain"
      data-state={state}
    >
""" + blanket_jsx + """
    </div>
  );
}
"""

with open('src/components/PageCurtain.jsx', 'w', encoding='utf-8') as out:
    out.write(output_code)

print('Done generating PageCurtain.jsx! Length:', len(output_code))

