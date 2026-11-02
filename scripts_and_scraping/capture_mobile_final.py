import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

PAGES = [
    ("home", "http://localhost:5173/"),
    ("puppies", "http://localhost:5173/puppies"),
    ("puppy_detail", "http://localhost:5173/puppies/maltipoo-max-male"),
    ("contact", "http://localhost:5173/contact"),
    ("how_it_works", "http://localhost:5173/how-it-works"),
    ("happy_families", "http://localhost:5173/happy-families"),
    ("gone_home", "http://localhost:5173/gone-home"),
    ("faq", "http://localhost:5173/faq"),
]

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", {
        "width": 390,
        "height": 844,
        "deviceScaleFactor": 2,
        "mobile": True
    })

    for name, url in PAGES:
        driver.get(url)
        time.sleep(1.5)
        out = os.path.abspath(f"comparison/mobile/local/{name}.png")
        driver.save_screenshot(out)
        print(f"Saved mobile {name} to {out}")

finally:
    driver.quit()

print("All mobile screenshots updated!")
