with open('scripts_and_scraping/pup_stage_code.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'f\.(setPose|stride|face|walkedTo|lookAt|wag|hop|jolt|cock|yawn|woof|petting|reset|jump)', text)]
print('f method calls:', len(matches))
for idx in matches:
    print('--- CALL at', idx, '---')
    print(text[max(0, idx-50):min(len(text), idx+150)])

