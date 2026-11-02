with open('scripts_and_scraping/js_chunks/1wa3jfz4v5w2v.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('PupJourney')
# Grab 6000 chars before PupJourney and 4000 after
start = max(0, idx - 6500)
end = min(len(text), idx + 4500)

with open('scripts_and_scraping/exact_pup_journey_core.js', 'w', encoding='utf-8') as out:
    out.write(text[start:end])

print(f'Wrote exact_pup_journey_core.js ({end-start} bytes)')

