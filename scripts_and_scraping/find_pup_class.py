with open('scripts_and_scraping/js_chunks/1llon2cx5n3pm.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('new n.f(')
if idx == -1:
    idx = text.find('.f(')
print('new .f index:', idx)
print(text[idx-200:idx+300])

