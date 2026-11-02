from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)

try:
    driver.get('https://puppy.instabizweb.com/')
    lenis_check = driver.execute_script('''
        return {
            hasLenis: !!window.lenis,
            lenisKeys: window.lenis ? Object.keys(window.lenis) : null,
            htmlClass: document.documentElement.className,
            bodyClass: document.body.className
        };
    ''')
    print('Lenis check on live site:', lenis_check)
finally:
    driver.quit()

