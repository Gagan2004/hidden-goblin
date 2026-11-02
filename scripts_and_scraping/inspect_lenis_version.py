with open('scripts_and_scraping/js_chunks/04u0_mknmf3rz.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('lenisVersion')
print('lenisVersion idx:', idx)
print(text[idx-200:idx+600])

