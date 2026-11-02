import subprocess
import os

PAGES = [
    ('puppies', 'https://puppy.instabizweb.com/puppies'),
    ('how-it-works', 'https://puppy.instabizweb.com/how-it-works'),
    ('happy-families', 'https://puppy.instabizweb.com/happy-families'),
    ('gone-home', 'https://puppy.instabizweb.com/gone-home'),
    ('faq', 'https://puppy.instabizweb.com/faq'),
    ('contact', 'https://puppy.instabizweb.com/contact'),
    ('puppy-detail', 'https://puppy.instabizweb.com/puppies/maltipoo-max-male'),
]

os.makedirs('screenshots', exist_ok=True)
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

for name, url in PAGES:
    out = os.path.abspath(f'screenshots/{name}.png')
    cmd = [chrome, '--headless=new', '--window-size=1440,2500', f'--screenshot={out}', url]
    print(f"Capturing {name} -> {out}...")
    try:
        subprocess.run(cmd, timeout=30, check=True)
        print(f" Captured {name}.png ({os.path.getsize(out)} bytes)")
    except Exception as e:
        print(f" Error capturing {name}: {e}")

