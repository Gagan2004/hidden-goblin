import re

with open('all_styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

scenes = ['tp-hero', 'tp-meet', 'tp-paths', 'tp-chat', 'tp-passport', 'tp-dusk', 'tp-night', 'tp-home']

for s in scenes:
    matches = re.findall(rf'(\.{s}[^\{{]*\{{[^\}}]+\}})', css)
    print(f"\n=== {s} ({len(matches)} rules) ===")
    for m in matches[:3]:
        print(m[:200])

