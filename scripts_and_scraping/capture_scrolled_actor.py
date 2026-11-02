import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless=new')
options.add_argument('--window-size=1440,900')
driver = webdriver.Chrome(options=options)

try:
    driver.get('http://localhost:5173/')
    time.sleep(2.0)
    driver.execute_script('window.scrollTo(0, 950);')
    time.sleep(1.0)
    driver.save_screenshot('comparison/desktop/local/scroll_actor_live.png')
    print('Saved scroll_actor_live.png')
finally:
    driver.quit()

