with open('scripts_and_scraping/js_chunks/1wa3jfz4v5w2v.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('pup-actor')
print('pup-actor at:', idx)
print(text[idx-3000:idx+2500])

