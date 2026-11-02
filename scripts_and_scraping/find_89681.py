with open('scripts_and_scraping/js_chunks/1llon2cx5n3pm.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'89681', text)]
print('89681 occurrences:', len(matches))
for idx in matches:
    print('--- MATCH at', idx, '---')
    print(text[max(0, idx-50):min(len(text), idx+300)])

