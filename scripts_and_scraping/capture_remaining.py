import subprocess
import os

PAGES = [
    ('happy-families', 'https://puppy.instabizweb.com/happy-families'),
    ('contact', 'https://puppy.instabizweb.com/contact'),
    ('puppy-detail', 'https://puppy.instabizweb.com/puppies/maltipoo-max-male'),
]

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

for name, url in PAGES:
    out = os.path.abspath(f'screenshots/{name}.png')
    cmd = [
        chrome,
        '--headless=new',
        '--window-size=1440,2500',
        '--disable-gpu',
        '--disable-extensions',
        f'--screenshot={out}',
        url
    ]
    print(f"Capturing {name}...")
    try:
        res = subprocess.run(cmd, timeout=15, capture_output=True)
        print(f" Captured {name}.png: exists={os.path.exists(out)}")
    except Exception as e:
        print(f" Error capturing {name}: {e}")

