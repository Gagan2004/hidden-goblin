with open('scripts_and_scraping/js_chunks/1wa3jfz4v5w2v.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('pup-actor')
start_idx = text.rfind('function', 0, idx)
# take until the end of this chunk
with open('scripts_and_scraping/pup_stage_code.js', 'w', encoding='utf-8') as out:
    out.write(text[start_idx:])
print('Wrote pup_stage_code.js, length:', len(text[start_idx:]))
