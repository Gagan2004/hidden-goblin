from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=1440,900")
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=chrome_options)
try:
    # Test 3: Contact Letter Form
    print("--- Test 3: Contact Letter Form ---")
    driver.get("http://localhost:4173/contact")
    time.sleep(1)

    driver.execute_script("""
        const nameInput = document.querySelector('input[placeholder="your full name"]');
        const phoneInput = document.querySelector('input[placeholder="+971 50 123 4567"]');
        if (nameInput) {
            const nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
            nativeInputValueSetter.call(nameInput, 'Sarah Jenkins');
            nameInput.dispatchEvent(new Event('input', { bubbles: true }));
        }
        if (phoneInput) {
            const nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
            nativeInputValueSetter.call(phoneInput, '+971 50 123 4567');
            phoneInput.dispatchEvent(new Event('input', { bubbles: true }));
        }
    """)
    time.sleep(0.5)

    submit_btn = driver.find_element(By.XPATH, "//button[contains(., 'Post my letter')]")
    driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
    time.sleep(0.3)
    submit_btn.click()
    time.sleep(1)

    success_msg = driver.find_elements(By.XPATH, "//*[contains(text(), 'Your letter is on its way')]")
    print(f"Success banner found: {len(success_msg) > 0}")
    assert len(success_msg) > 0, "Letter sent confirmation should appear"
    out_letter = os.path.abspath("screenshots_clone/interactive_letter_sent.png")
    driver.save_screenshot(out_letter)
    print(f"Saved letter submitted screenshot: {out_letter}")
    print(" Contact form test PASSED!")

finally:
    driver.quit()
