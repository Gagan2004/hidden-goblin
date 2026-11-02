with open('scripts_and_scraping/exact_pup_journey_core.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function T(')
print('T(e) found at:', idx)
print('Before T(e):')
print(text[max(0, idx-1500):idx])

