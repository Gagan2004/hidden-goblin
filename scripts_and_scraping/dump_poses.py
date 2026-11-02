with open('scripts_and_scraping/js_chunks/1llon2cx5n3pm.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('1063,')
print('1063 index:', idx)
with open('scripts_and_scraping/exact_poses.js', 'w', encoding='utf-8') as out:
    out.write(text[idx:idx+8000])

print('Wrote exact_poses.js (8KB)')

