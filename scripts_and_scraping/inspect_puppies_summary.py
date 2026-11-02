import json

with open('puppies_data.json', 'r', encoding='utf-8') as f:
    puppies = json.load(f)

print(f"Total puppies: {len(puppies)}")
available = [p for p in puppies if p['status'] == 'available']
gone = [p for p in puppies if p['status'] == 'gone_home']
print(f"Available: {len(available)}, Gone home: {len(gone)}")

for p in puppies[:15]:
    print(f"- {p['name']} ({p['slug']}): images={len(p['images'])} video={bool(p['video'])} status={p['status']}")

