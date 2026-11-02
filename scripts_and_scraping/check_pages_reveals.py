import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless=new')
options.add_argument('--window-size=1440,900')
driver = webdriver.Chrome(options=options)

try:
    driver.get('http://localhost:5173/puppies')
    time.sleep(1.8)
    revealed_puppies = driver.find_elements(By.CSS_SELECTOR, '[data-revealed="true"]')
    total_puppies = driver.find_elements(By.CSS_SELECTOR, '[data-reveal]')
    print(f'PuppiesPage: {len(revealed_puppies)} / {len(total_puppies)} revealed')

    driver.get('http://localhost:5173/happy-families')
    time.sleep(1.8)
    revealed_hf = driver.find_elements(By.CSS_SELECTOR, '[data-revealed="true"]')
    total_hf = driver.find_elements(By.CSS_SELECTOR, '[data-reveal]')
    print(f'HappyFamiliesPage: {len(revealed_hf)} / {len(total_hf)} revealed')

    driver.get('http://localhost:5173/gone-home')
    time.sleep(1.8)
    revealed_gh = driver.find_elements(By.CSS_SELECTOR, '[data-revealed="true"]')
    total_gh = driver.find_elements(By.CSS_SELECTOR, '[data-reveal]')
    print(f'GoneHomePage: {len(revealed_gh)} / {len(total_gh)} revealed')

    driver.get('http://localhost:5173/faq')
    time.sleep(1.8)
    revealed_faq = driver.find_elements(By.CSS_SELECTOR, '[data-revealed="true"]')
    total_faq = driver.find_elements(By.CSS_SELECTOR, '[data-reveal]')
    print(f'FaqPage: {len(revealed_faq)} / {len(total_faq)} revealed')

finally:
    driver.quit()

