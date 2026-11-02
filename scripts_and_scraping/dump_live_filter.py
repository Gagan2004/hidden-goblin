from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--headless=new')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)
try:
    driver.get('https://puppy.instabizweb.com/puppies')
    time.sleep(2)

    filter_html = driver.execute_script("""
        // Find element containing 'Everywhere'
        const buttons = Array.from(document.querySelectorAll('button'));
        const btn = buttons.find(b => b.textContent.includes('Everywhere'));
        if (btn) {
            // Find parent board/container
            let p = btn.parentElement;
            while (p && !p.className.includes('tp-board') && !p.className.includes('filter') && p.tagName !== 'SECTION') {
                p = p.parentElement;
            }
            return p ? p.outerHTML : btn.parentElement.outerHTML;
        }
        return 'Not found';
    """)
    print("Filter found, length:", len(filter_html))
    with open('live_puppies_filter_card.html', 'w', encoding='utf-8') as f:
        f.write(filter_html)
    print("Saved live_puppies_filter_card.html")
finally:
    driver.quit()
