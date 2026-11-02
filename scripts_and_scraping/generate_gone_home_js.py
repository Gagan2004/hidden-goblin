import json

with open('extracted_gone_home.json', 'r', encoding='utf-8') as f:
    tickets = json.load(f)

# Deduplicate by (name, meta)
seen = set()
clean_tickets = []
for t in tickets:
    key = (t['name'], t['meta'])
    if key not in seen and t['name']:
        seen.add(key)
        clean_tickets.append(t)

with open('src/data/goneHome.js', 'w', encoding='utf-8') as f:
    f.write('export const GONE_HOME_TICKETS = ' + json.dumps(clean_tickets, indent=2, ensure_ascii=False) + ';\n')

print("Saved src/data/goneHome.js with", len(clean_tickets), "unique tickets")

