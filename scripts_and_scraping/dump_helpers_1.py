with open('scripts_and_scraping/pup_journey_complete.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('PupJourney')
before = text[:idx]

# Let's inspect from function w( onwards
w_idx = before.find('function w(')
if w_idx == -1:
    w_idx = 0

print('Code from helper start to PupJourney:')
print(before[w_idx:w_idx+4000])

