with open('scripts_and_scraping/js_chunks/1llon2cx5n3pm.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('peekaboo')
print('peekaboo idx:', idx)
print(text[idx-200:idx+1500].encode('ascii', errors='replace').decode('ascii'))
