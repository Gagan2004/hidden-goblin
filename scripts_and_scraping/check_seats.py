with open('src/pages/HomePage.jsx', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<li className="tp-lineup__seat"', text)
print('Total tp-lineup__seat:', len(matches))

