import subprocess
import os

PAGES = [
    ('mobile_home', 'http://localhost:4173/'),
    ('mobile_puppies', 'http://localhost:4173/puppies'),
    ('mobile_puppy_detail', 'http://localhost:4173/puppies/maltipoo-max-male'),
    ('mobile_contact', 'http://localhost:4173/contact'),
]

os.makedirs('screenshots_clone/mobile', exist_ok=True)
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

for name, url in PAGES:
    out = os.path.abspath(f'screenshots_clone/mobile/{name}.png')
    cmd = [
        chrome,
        '--headless=new',
        '--window-size=390,844',
        '--disable-gpu',
        f'--screenshot={out}',
        url
    ]
    print(f"Capturing mobile {name}...")
    try:
        subprocess.run(cmd, timeout=15, check=True)
        print(f" Saved {name}.png ({os.path.getsize(out)} bytes)")
    except Exception as e:
        print(f" Error {name}: {e}")

print("Done capturing mobile screenshots!")

