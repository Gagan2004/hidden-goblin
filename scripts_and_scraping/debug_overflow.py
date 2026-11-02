from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=390,844")
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=chrome_options)
try:
    driver.get("http://localhost:4173/")
    time.sleep(1)

    res = driver.execute_script("""
        const innerWidth = window.innerWidth;
        const scrollWidth = document.documentElement.scrollWidth;
        const bodyScrollWidth = document.body.scrollWidth;

        const overflowing = [];
        const allElements = document.querySelectorAll('*');
        for (const el of allElements) {
            const rect = el.getBoundingClientRect();
            if (rect.right > innerWidth + 2) {
                overflowing.push({
                    tag: el.tagName,
                    id: el.id,
                    className: el.className ? String(el.className).substring(0, 80) : '',
                    right: rect.right,
                    width: rect.width
                });
            }
        }

        // Header info
        const header = document.querySelector('header');
        const headerRect = header ? header.getBoundingClientRect() : null;
        const nav = document.querySelector('header nav');
        const navDisplay = nav ? window.getComputedStyle(nav).display : null;
        const menuBtn = document.querySelector('header button[aria-label="Open menu"]');
        const menuBtnRect = menuBtn ? menuBtn.getBoundingClientRect() : null;

        return {
            innerWidth,
            scrollWidth,
            bodyScrollWidth,
            overflowCount: overflowing.length,
            overflowing: overflowing.slice(0, 10),
            headerRect,
            navDisplay,
            menuBtnRect
        };
    """)

    import json
    print(json.dumps(res, indent=2))
finally:
    driver.quit()

