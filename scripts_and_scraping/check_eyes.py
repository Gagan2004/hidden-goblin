with open('src/pages/HomePage.jsx', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print('open count:', len(re.findall(r'data-p=["\']open["\']', text)))
print('shut count:', len(re.findall(r'data-p=["\']shut["\']', text)))
print('eyes count:', len(re.findall(r'data-p=["\']eyes["\']', text)))

