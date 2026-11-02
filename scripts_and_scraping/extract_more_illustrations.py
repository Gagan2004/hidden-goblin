from bs4 import BeautifulSoup
import os

files_to_check = ['rendered_home.html', 'scraped_pages/how-it-works.html', 'scraped_pages/gone-home.html', 'scraped_pages/contact.html', 'scraped_pages/faq.html']

for fpath in files_to_check:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    for name in ['tp-booth', 'tp-postcard', 'tp-flight', 'tp-house', 'tp-letterform', 'tp-board', 'tp-lamp']:
        el = soup.find(class_=lambda c: c and name in str(c))
        out_name = f"{name}.html"
        if el and not os.path.exists(out_name):
            with open(out_name, 'w', encoding='utf-8') as out:
                out.write(str(el))
            print(f"Saved {out_name} ({len(str(el))} bytes) from {fpath}")

