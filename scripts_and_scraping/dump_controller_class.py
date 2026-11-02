with open('scripts_and_scraping/js_chunks/1llon2cx5n3pm.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Find module 89681
idx = text.find('89681')
print('89681 index:', idx)

# Find where class/function starts
start = text.rfind('function', 0, idx)
end = text.find('function', idx + 100)

with open('scripts_and_scraping/pup_controller_class.js', 'w', encoding='utf-8') as out:
    out.write(text[idx:idx+7000])

print('Wrote pup_controller_class.js (7KB)')

