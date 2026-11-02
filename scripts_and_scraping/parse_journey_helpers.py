with open('scripts_and_scraping/pup_journey_complete.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find where PupJourney is defined:
idx = text.find('PupJourney')
# Let's look before PupJourney to find the helper functions
before = text[:idx]
print('Functions before PupJourney:')
import re
for m in re.finditer(r'function\s+([a-zA-Z0-9_$]+)\s*\(|([a-zA-Z0-9_$]+)\s*=\s*(?:function|\([^)]*\)\s*=>)', before):
    print(m.group(0))

