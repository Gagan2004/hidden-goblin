import re

with open('scripts_and_scraping/js_chunks/1llon2cx5n3pm.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('89681')
print('89681 idx:', idx)
if idx != -1:
    print(text[idx-50:idx+2500])

