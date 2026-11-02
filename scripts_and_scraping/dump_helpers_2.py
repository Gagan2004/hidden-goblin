with open('scripts_and_scraping/pup_journey_complete.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('PupJourney')
before = text[:idx]

# Let's inspect the 4000 characters before PupJourney
print(before[-4000:])

