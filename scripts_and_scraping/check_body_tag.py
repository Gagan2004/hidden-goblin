with open('src/components/PupJourney.jsx', 'r', encoding='utf-8') as f:
    text = f.read()

import re
body_match = re.search(r'<g data-p="body"[^>]*>', text)
if body_match:
    print('Body tag in PupJourney.jsx:')
    print(body_match.group(0))

idx = text.find('data-p="body"')
print(text[idx-50:idx+300])

