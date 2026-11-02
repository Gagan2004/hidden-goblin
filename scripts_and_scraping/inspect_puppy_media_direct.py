import re
from urllib.parse import unquote

with open('scraped_puppies/maltipoo-max-male.html', 'r', encoding='utf-8') as f:
    content = f.read()

# search for /media/
medias = set(re.findall(r'(/media/[^"\'\s>&]+)', content))
print(f"Total media matches in maltipoo-max-male: {len(medias)}")
for m in sorted(medias):
    print(" -", unquote(m))

