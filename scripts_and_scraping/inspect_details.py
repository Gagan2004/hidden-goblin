import os
from bs4 import BeautifulSoup

def inspect(name, path):
    print(f"\n=================== {name} ===================")
    with open(path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    page = soup.find('div', class_='tp-page')
    if not page:
        print("No tp-page found")
        return
    for i, child in enumerate(page.find_all(recursive=False)):
        cls = child.get('class', [])
        print(f"Page child {i}: <{child.name} class='{' '.join(cls)}'>")

inspect("puppies.html", "scripts_and_scraping/scraped_pages/puppies.html")
inspect("how-it-works.html", "scripts_and_scraping/scraped_pages/how-it-works.html")
inspect("happy-families.html", "scripts_and_scraping/scraped_pages/happy-families.html")
inspect("gone-home.html", "scripts_and_scraping/scraped_pages/gone-home.html")
inspect("faq.html", "scripts_and_scraping/scraped_pages/faq.html")
inspect("contact.html", "scripts_and_scraping/scraped_pages/contact.html")
inspect("maltipoo-max-male.html", "scripts_and_scraping/scraped_puppies/maltipoo-max-male.html")
