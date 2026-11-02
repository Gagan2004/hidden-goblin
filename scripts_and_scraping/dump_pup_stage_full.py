with open('scripts_and_scraping/js_chunks/1wa3jfz4v5w2v.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('PupStage')
if idx == -1:
    idx = text.find('pup-actor')
print('Index:', idx)
print(text[idx-6000:idx])

