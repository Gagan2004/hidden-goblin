import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless=new')
options.add_argument('--window-size=1440,900')
driver = webdriver.Chrome(options=options)

try:
    # 1. Homepage after curtain lifts
    driver.get('http://localhost:5173/')
    time.sleep(2.0)
    driver.save_screenshot('comparison/desktop/local/homepage_synced.png')
    print('Captured homepage_synced.png')

    # 2. Puppies page
    driver.get('http://localhost:5173/puppies')
    time.sleep(2.0)
    driver.save_screenshot('comparison/desktop/local/puppies_synced.png')
    print('Captured puppies_synced.png')

    # 3. Happy Families
    driver.get('http://localhost:5173/happy-families')
    time.sleep(2.0)
    driver.save_screenshot('comparison/desktop/local/happy_families_synced.png')
    print('Captured happy_families_synced.png')

    # 4. Gone Home
    driver.get('http://localhost:5173/gone-home')
    time.sleep(2.0)
    driver.save_screenshot('comparison/desktop/local/gone_home_synced.png')
    print('Captured gone_home_synced.png')

finally:
    driver.quit()

