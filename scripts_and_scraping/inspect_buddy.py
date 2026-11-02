import re

with open('scripts_and_scraping/js_chunks/1llon2cx5n3pm.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('PupBuddy')
print('PupBuddy idx:', idx)
print(text[idx-500:idx+1500])

