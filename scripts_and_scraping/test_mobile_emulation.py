from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=chrome_options)
try:
    # Set mobile emulation via CDP
    driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", {
        "width": 390,
        "height": 844,
        "deviceScaleFactor": 2,
        "mobile": True
    })

    driver.get("http://localhost:4173/")
    time.sleep(1)

    info = driver.execute_script("""
        const menuBtn = document.querySelector('header button[aria-label="Open menu"]');
        const menuBtnRect = menuBtn ? menuBtn.getBoundingClientRect() : null;
        return {
            innerWidth: window.innerWidth,
            scrollWidth: document.documentElement.scrollWidth,
            menuBtnRect: menuBtnRect
        };
    """)
    print("Mobile viewport info with CDP:", info)

    out = os.path.abspath("screenshots_clone/mobile/mobile_home_emulated.png")
    driver.save_screenshot(out)
    print("Saved screenshot to", out, "size:", os.path.getsize(out))
finally:
    driver.quit()
