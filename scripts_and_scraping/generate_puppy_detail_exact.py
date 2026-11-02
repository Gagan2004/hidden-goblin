import re
from bs4 import BeautifulSoup
from html_to_jsx_helper import html_to_jsx

with open('extracted_puppy_stream.html', 'r', encoding='utf-8') as f:
    c = f.read()

start_idx = c.find('<article')
end_idx = c.rfind('</article>') + len('</article>')
article_html = c[start_idx:end_idx]

jsx_body = html_to_jsx(article_html)

template = f"""import React, {{ useState }} from 'react';
import {{ PUPPIES }} from '../data/puppies';

export default function PuppyDetailPage({{ slug, navigate, onWatchVideo }}) {{
  const puppy = PUPPIES.find((p) => p.slug === slug) || PUPPIES[0];
  const [selectedImgIdx, setSelectedImgIdx] = useState(0);

  return (
    <div className="relative pt-[var(--header-h)] outline-none" id="main" tabIndex="-1">
      {jsx_body}
    </div>
  );
}}
"""

with open('src/pages/PuppyDetailPage.jsx', 'w', encoding='utf-8') as out:
    out.write(template)

print("Generated exact PuppyDetailPage.jsx successfully!")
