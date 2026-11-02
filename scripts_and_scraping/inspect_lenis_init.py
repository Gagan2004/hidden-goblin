with open('scripts_and_scraping/js_chunks/04u0_mknmf3rz.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'new\s+Lenis|new\s+\w+\.Lenis|\.lenis\s*=', text)]
print('Lenis init matches in 04u0:', len(matches))
for idx in matches:
    print('--- MATCH ---')
    print(text[max(0, idx-100):min(len(text), idx+300)])

