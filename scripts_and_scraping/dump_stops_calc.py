with open('scripts_and_scraping/js_chunks/1wa3jfz4v5w2v.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('pup-actor')
print('pup-actor at:', idx)
# Find the start of the function containing stops / T($)
start_idx = text.rfind('function', 0, idx - 3000)
print('start_idx:', start_idx)
with open('scripts_and_scraping/pup_stage_stops.js', 'w', encoding='utf-8') as out:
    out.write(text[start_idx:idx])
print('Wrote pup_stage_stops.js, length:', idx - start_idx)

