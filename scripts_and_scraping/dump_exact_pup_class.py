with open('scripts_and_scraping/js_chunks/1llon2cx5n3pm.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's write the controller class from 4000 to 10200
with open('scripts_and_scraping/exact_pup_class.js', 'w', encoding='utf-8') as out:
    out.write(text[4000:10200])

print('Wrote exact_pup_class.js (6.2KB)')

