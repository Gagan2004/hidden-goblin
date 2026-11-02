from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

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

    # 1. Test clicking the mobile menu button
    driver.get("http://localhost:4173/")
    time.sleep(1)

    menu_btn = driver.find_element(By.CSS_SELECTOR, 'header button[aria-label="Open menu"]')
    menu_btn.click()
    time.sleep(0.5)

    out_menu = os.path.abspath("screenshots_clone/mobile/mobile_menu_open.png")
    driver.save_screenshot(out_menu)
    print("Saved mobile menu screenshot:", out_menu)

    # 2. Capture mobile puppies page
    driver.get("http://localhost:4173/puppies")
    time.sleep(1)
    out_puppies = os.path.abspath("screenshots_clone/mobile/mobile_puppies.png")
    driver.save_screenshot(out_puppies)
    print("Saved mobile puppies:", out_puppies)

    # 3. Capture mobile puppy detail page
    driver.get("http://localhost:4173/puppies/maltipoo-max-male")
    time.sleep(1)
    out_detail = os.path.abspath("screenshots_clone/mobile/mobile_puppy_detail.png")
    driver.save_screenshot(out_detail)
    print("Saved mobile puppy detail:", out_detail)

    # 4. Capture mobile contact page
    driver.get("http://localhost:4173/contact")
    time.sleep(1)
    out_contact = os.path.abspath("screenshots_clone/mobile/mobile_contact.png")
    driver.save_screenshot(out_contact)
    print("Saved mobile contact:", out_contact)

    # 5. Capture mobile how it works
    driver.get("http://localhost:4173/how-it-works")
    time.sleep(1)
    out_how = os.path.abspath("screenshots_clone/mobile/mobile_how_it_works.png")
    driver.save_screenshot(out_how)
    print("Saved mobile how-it-works:", out_how)

    # 6. Capture mobile faq
    driver.get("http://localhost:4173/faq")
    time.sleep(1)
    out_faq = os.path.abspath("screenshots_clone/mobile/mobile_faq.png")
    driver.save_screenshot(out_faq)
    print("Saved mobile faq:", out_faq)

    # 7. Capture mobile happy families
    driver.get("http://localhost:4173/happy-families")
    time.sleep(1)
    out_hf = os.path.abspath("screenshots_clone/mobile/mobile_happy_families.png")
    driver.save_screenshot(out_hf)
    print("Saved mobile happy families:", out_hf)

finally:
    driver.quit()
print("All mobile screenshots updated successfully!")
