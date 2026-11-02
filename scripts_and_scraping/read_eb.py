with open('scripts_and_scraping/exact_pup_journey_core.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('eb=')
print('eb found at:', idx)
print(text[idx:idx+2500])

