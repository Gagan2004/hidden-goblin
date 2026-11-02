import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless=new')
options.add_argument('--window-size=1440,900')
driver = webdriver.Chrome(options=options)

try:
    driver.get('http://localhost:5173/happy-families')
    time.sleep(1.5)
    initial_revealed = len(driver.find_elements(By.CSS_SELECTOR, '[data-revealed="true"]'))
    print(f'Initial revealed: {initial_revealed}')

    driver.execute_script('window.scrollTo(0, 2500);')
    time.sleep(0.8)
    after_scroll_revealed = len(driver.find_elements(By.CSS_SELECTOR, '[data-revealed="true"]'))
    print(f'After scroll revealed: {after_scroll_revealed}')
    assert after_scroll_revealed > initial_revealed, 'Expected more elements revealed on scroll'
    print('PASS: Scroll revealing triggers dynamically as user scrolls!')
finally:
    driver.quit()

