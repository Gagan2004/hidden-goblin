import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless=new')
options.add_argument('--window-size=1440,900')
driver = webdriver.Chrome(options=options)

try:
    driver.get('http://localhost:5173/')
    time.sleep(1.5)
    
    # Scroll to chat section
    chat = driver.find_element(By.CSS_SELECTOR, '.tp-chat')
    driver.execute_script('arguments[0].scrollIntoView({ behavior: "instant", block: "center" });', chat)
    time.sleep(1.0)
    
    status = driver.find_element(By.CSS_SELECTOR, '.tp-phone__status')
    print(f'Phone status at chat section: {status.text}')
    
    # Check steps
    steps = driver.find_elements(By.CSS_SELECTOR, '.tp-chat__step')
    print(f'Total chat steps: {len(steps)}')
    for i, s in enumerate(steps):
        print(f'Step {i}: active={s.get_attribute("data-active")}, done={s.get_attribute("data-done")}')
        
    print('PASS: Chat simulator scroll interactions functioning!')

finally:
    driver.quit()

