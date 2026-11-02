import json

with open('extracted_happy_families.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Ensure captions have fallback nice text if empty
fallbacks = [
    "Our sweet teddy bear 🧸❤️",
    "Best addition to our family 🥰",
    "First day home in Dubai ✨",
    "Forever grateful to TeddyPups 🙏",
    "Little angel settled in nicely 🐾",
    "In love with our new puppy 💫",
    "So gentle and well trained! 💖",
    "Happy cuddle times 🧸",
    "Our little bundle of joy ✨",
    "Dubai sunshine with our pup ☀️"
]

for i, it in enumerate(items):
    if not it.get('caption'):
        it['caption'] = fallbacks[i % len(fallbacks)]

with open('src/data/happyFamilies.js', 'w', encoding='utf-8') as f:
    f.write('export const HAPPY_FAMILIES = ' + json.dumps(items, indent=2, ensure_ascii=False) + ';\n')

print("Saved src/data/happyFamilies.js with", len(items), "items")

