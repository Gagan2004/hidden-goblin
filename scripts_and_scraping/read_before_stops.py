with open('scripts_and_scraping/js_chunks/1wa3jfz4v5w2v.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = 29166
print('Before 29166:')
print(text[max(0, idx-4000):idx])

