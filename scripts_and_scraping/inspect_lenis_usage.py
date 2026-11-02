with open('scripts_and_scraping/js_chunks/3gnj9-_12x8lt.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('lenis')
print('lenis in 3gnj9:', idx)
if idx != -1:
    print(text[max(0, idx-100):min(len(text), idx+600)])
