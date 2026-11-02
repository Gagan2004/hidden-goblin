with open('scripts_and_scraping/js_chunks/1wa3jfz4v5w2v.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'pup-actor|pup-layer|PupStage', text)]
print('Matches:', len(matches))
for idx in matches:
    print('--- MATCH ---')
    print(text[max(0, idx-100):min(len(text), idx+600)])

