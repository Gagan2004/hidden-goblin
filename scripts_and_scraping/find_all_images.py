import re

with open('scraped_home.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's search for all src attributes
srcs = set(re.findall(r'src=["\']([^"\']+)["\']', html))
print(f"Total src attributes: {len(srcs)}")
for s in sorted(srcs):
    if not s.endswith('.js'):
        print(" src:", s[:100])

# Let's search for all background images or media URLs
medias = set(re.findall(r'/(?:media|_next/image|_next/static)[^"\'\s)]+', html))
print(f"Total media/image links: {len(medias)}")
for m in sorted(medias)[:20]:
    print(" media:", m[:100])

