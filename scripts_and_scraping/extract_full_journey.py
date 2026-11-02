with open('scripts_and_scraping/js_chunks/1wa3jfz4v5w2v.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Find PupJourney export
idx = text.find('PupJourney')
print('PupJourney export index:', idx)

# Find the start of the module containing PupJourney
# Usually starts with a webpack/turbopack module definition or closure
mod_start = text.rfind('e.s([', 0, idx)
print('mod_start:', mod_start)

# Let's find all code in 1wa3jfz4v5w2v.js from 15000 to 40000
with open('scripts_and_scraping/pup_journey_complete.js', 'w', encoding='utf-8') as out:
    out.write(text[15000:40000])

print('Wrote pup_journey_complete.js (25KB)')

