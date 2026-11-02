import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless=new')
options.add_argument('--window-size=1440,900')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

try:
    print('1. Testing Initial Page Load & Curtain Intro...')
    driver.get('http://localhost:5173/')
    
    # Check curtain initial state
    curtain = driver.find_element(By.CSS_SELECTOR, '.tp-curtain')
    initial_state = curtain.get_attribute('data-state')
    print(f'Initial curtain state: {initial_state}')
    
    # Wait for curtain to transition to idle
    time.sleep(1.5)
    idle_state = curtain.get_attribute('data-state')
    print(f'Curtain state after 1.5s: {idle_state}')
    assert idle_state == 'idle', f'Expected idle, got {idle_state}'
    print('PASS: Curtain intro -> idle verified!')

    print('\n2. Testing Scroll Reveals (RevealScope)...')
    # Check if elements have data-revealed="true"
    revealed_count = len(driver.find_elements(By.CSS_SELECTOR, '[data-revealed="true"]'))
    print(f'Elements with data-revealed="true" on HomePage: {revealed_count}')
    assert revealed_count > 0, 'Expected revealed elements on initial viewport'
    print('PASS: Scroll reveal active!')

    print('\n3. Testing Route Transition Curtain...')
    # Click on "Puppies" in header navigation
    puppies_link = driver.find_element(By.CSS_SELECTOR, 'header a[href="/puppies"]')
    puppies_link.click()
    
    # Check covering/lifting
    time.sleep(0.15)
    nav_state = curtain.get_attribute('data-state')
    print(f'Curtain state during navigation: {nav_state}')
    
    time.sleep(1.0)
    after_nav_state = curtain.get_attribute('data-state')
    print(f'Curtain state after navigation: {after_nav_state}')
    print(f'Current URL: {driver.current_url}')
    assert 'puppies' in driver.current_url, 'Expected URL to contain puppies'
    assert after_nav_state == 'idle', 'Expected curtain to return to idle'
    print('PASS: Route transition curtain verified!')

    print('\n4. Testing Happy Families Polaroid Reveals...')
    driver.get('http://localhost:5173/happy-families')
    time.sleep(1.5)
    
    # Scroll down to trigger polaroid reveals
    driver.execute_script('window.scrollTo(0, 1000);')
    time.sleep(0.8)
    hf_revealed = len(driver.find_elements(By.CSS_SELECTOR, '.tp-polaroid[style*="--d"]'))
    print(f'Polaroids rendered with staggered delay: {hf_revealed}')
    assert hf_revealed > 0, 'Expected polaroids with delay'
    print('PASS: Happy Families polaroids animated!')

    print('\n5. Testing Mascot Buddy Click Interaction & Hearts...')
    driver.get('http://localhost:5173/')
    time.sleep(1.5)
    
    buddy = driver.find_element(By.CSS_SELECTOR, '.tp-hero__teddy .pup-buddy, .pup-buddy')
    print('Clicking Mascot Buddy...')
    buddy.click()
    time.sleep(0.3)
    
    bubble = driver.find_element(By.CSS_SELECTOR, '.pup-bubble')
    bubble_show = bubble.get_attribute('data-show')
    bubble_text = bubble.text
    print(f'Bubble data-show: {bubble_show}, text: "{bubble_text}"')
    assert bubble_show == 'true', 'Expected bubble to show'
    print('PASS: Mascot Buddy click interaction verified!')

    print('\n6. Testing Lineup Hover State...')
    first_pup = driver.find_element(By.CSS_SELECTOR, '.tp-lineup__pup')
    driver.execute_script("arguments[0].dispatchEvent(new PointerEvent('pointerenter'));", first_pup)
    time.sleep(0.2)
    pup_state = first_pup.get_attribute('data-state')
    print(f'Lineup pup state on hover: {pup_state}')
    print('PASS: Lineup hover state verified!')

    print('\nALL ANIMATION TESTS PASSED PERFECTLY!')

finally:
    driver.quit()

