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
    # Test 1: Puppies page filter
    print("--- Test 1: Puppies filter ---")
    driver.get("http://localhost:4173/puppies")
    time.sleep(1)

    initial_cards = driver.find_elements(By.CSS_SELECTOR, 'div.group.relative')
    print(f"Initial puppy cards count: {len(initial_cards)}")

    # Click Pomeranian filter button
    pom_btn = None
    for btn in driver.find_elements(By.CSS_SELECTOR, 'button'):
        if btn.text.strip() == 'Pomeranian':
            pom_btn = btn
            break

    if pom_btn:
        pom_btn.click()
        time.sleep(0.5)
        filtered_cards = driver.find_elements(By.CSS_SELECTOR, 'div.group.relative')
        print(f"Filtered puppy cards (Pomeranian) count: {len(filtered_cards)}")
        assert len(filtered_cards) > 0 and len(filtered_cards) < len(initial_cards), "Filtering should reduce card count!"
        print(" Filter test PASSED!")

    # Test 2: Video Modal
    print("\n--- Test 2: Video modal ---")
    driver.get("http://localhost:4173/puppies/maltipoo-max-male")
    time.sleep(1)

    video_btn = driver.find_element(By.XPATH, "//button[contains(., 'Watch Video')]")
    video_btn.click()
    time.sleep(0.5)

    modal = driver.find_element(By.CSS_SELECTOR, "div[role='dialog']")
    assert modal is not None, "Video modal should be open"
    video_el = driver.find_element(By.CSS_SELECTOR, "div[role='dialog'] video")
    print(f"Video source in modal: {video_el.get_attribute('src')}")
    out_video = os.path.abspath("screenshots_clone/interactive_video_modal.png")
    driver.save_screenshot(out_video)
    print(f"Saved video modal screenshot: {out_video}")
    print(" Video modal test PASSED!")

    # Test 3: Contact Letter Form
    print("\n--- Test 3: Contact Letter Form ---")
    driver.get("http://localhost:4173/contact")
    time.sleep(1)

    letter_inputs = driver.find_elements(By.CSS_SELECTOR, "input")
    name_input = None
    phone_input = None
    for inp in letter_inputs:
        placeholder = inp.get_attribute("placeholder") or ""
        if "name" in placeholder.lower():
            name_input = inp
        elif "phone" in placeholder.lower() or "number" in placeholder.lower() or "whatsapp" in placeholder.lower():
            phone_input = inp

    if name_input:
        name_input.send_keys("Sarah Jenkins")
    if phone_input:
        phone_input.send_keys("+971 50 123 4567")

    # Click submit button
    submit_btn = driver.find_element(By.XPATH, "//button[contains(., 'Post my letter')]")
    driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
    time.sleep(0.3)
    submit_btn.click()
    time.sleep(0.8)

    # Check for success message
    success_msg = driver.find_elements(By.XPATH, "//*[contains(text(), 'Your letter is on its way')]")
    print(f"Success banner found: {len(success_msg) > 0}")
    assert len(success_msg) > 0, "Letter sent confirmation should appear"
    out_letter = os.path.abspath("screenshots_clone/interactive_letter_sent.png")
    driver.save_screenshot(out_letter)
    print(f"Saved letter submitted screenshot: {out_letter}")
    print(" Contact form test PASSED!")

    print("\nALL INTERACTIVE TESTS PASSED COMPLETELY! ")
finally:
    driver.quit()
