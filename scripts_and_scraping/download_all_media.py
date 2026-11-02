import urllib.request
import os
import time

with open('all_media_urls.txt', 'r', encoding='utf-8') as f:
    raw_urls = [line.strip() for line in f if line.strip()]

clean_urls = set()
for u in raw_urls:
    u = u.replace('\\', '/').strip(' "\'\/')
    u = u.replace('&amp;', '&')
    if u.startswith('media/') or u.startswith('brand/'):
        clean_urls.add('/' + u)

clean_urls = sorted(list(clean_urls))
print(f"Total clean media files: {len(clean_urls)}")

base_url = 'https://puppy.instabizweb.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

success = 0
skipped = 0
failed = 0

for i, rel_path in enumerate(clean_urls):
    parts = rel_path.lstrip('/').split('/')
    local_path = os.path.join('public', *parts)

    # Check if already downloaded as a file
    if os.path.isfile(local_path) and os.path.getsize(local_path) > 0:
        skipped += 1
        continue

    # Pre-create parent directory safely
    folder = os.path.dirname(local_path)
    os.makedirs(folder, exist_ok=True)

    full_url = base_url + rel_path
    downloaded = False
    for attempt in range(3):
        try:
            req = urllib.request.Request(full_url, headers=headers)
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = resp.read()
                with open(local_path, 'wb') as out_file:
                    out_file.write(data)
                downloaded = True
                success += 1
                break
        except Exception as e:
            time.sleep(0.3)

    if not downloaded:
        failed += 1
        print(f"Failed: {rel_path}")

    if (i + 1) % 25 == 0:
        print(f"Progress: {i+1}/{len(clean_urls)} (success={success}, skipped={skipped}, failed={failed})")

print(f"Download complete: {success} downloaded, {skipped} skipped, {failed} failed.")
