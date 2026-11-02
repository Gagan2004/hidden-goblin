import subprocess
import os

PAGES = [
    ('clone_home', 'http://localhost:4173/'),
    ('clone_puppies', 'http://localhost:4173/puppies'),
    ('clone_how_it_works', 'http://localhost:4173/how-it-works'),
    ('clone_happy_families', 'http://localhost:4173/happy-families'),
    ('clone_gone_home', 'http://localhost:4173/gone-home'),
    ('clone_faq', 'http://localhost:4173/faq'),
    ('clone_contact', 'http://localhost:4173/contact'),
    ('clone_puppy_detail', 'http://localhost:4173/puppies/maltipoo-max-male'),
]

os.makedirs('screenshots_clone', exist_ok=True)
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

for name, url in PAGES:
    out = os.path.abspath(f'screenshots_clone/{name}.png')
    cmd = [
        chrome,
        '--headless=new',
        '--window-size=1440,2500',
        '--disable-gpu',
        f'--screenshot={out}',
        url
    ]
    print(f"Capturing {name}...")
    try:
        subprocess.run(cmd, timeout=15, check=True)
        print(f" Saved {name}.png ({os.path.getsize(out)} bytes)")
    except Exception as e:
        print(f" Error {name}: {e}")

print("Done capturing clone screenshots!")

