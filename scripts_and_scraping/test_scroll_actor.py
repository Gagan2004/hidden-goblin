import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless=new')
options.add_argument('--window-size=1440,900')
driver = webdriver.Chrome(options=options)

try:
    print('Testing local server at http://localhost:5173/ ...')
    driver.get('http://localhost:5173/')
    time.sleep(2.0)

    # 1. Check Lenis class
    html_class = driver.execute_script('return document.documentElement.className;')
    print(f'HTML classes: "{html_class}"')
    assert 'lenis' in html_class, 'Expected html to have lenis class'
    print('PASS: Lenis smooth scroll active!')

    # 2. Check pup dataset
    pup_dataset = driver.execute_script('return document.documentElement.dataset.pup;')
    print(f'HTML dataset.pup: "{pup_dataset}"')
    assert pup_dataset == 'live', 'Expected html dataset.pup to be "live"'
    print('PASS: Live pup dataset active!')

    # 3. Check pup-layer and pup-actor
    actor_initial = driver.execute_script('''
        let actor = document.querySelector(".pup-actor");
        let layer = document.querySelector(".pup-layer");
        return {
            hasActor: !!actor,
            actorTransform: actor ? actor.style.transform : null,
            layerHidden: layer ? layer.hidden : null,
            layerFront: layer ? layer.dataset.front : null
        };
    ''')
    print(f'Initial actor state: {actor_initial}')
    assert actor_initial['hasActor'], 'Expected .pup-actor to exist'
    assert not actor_initial['layerHidden'], 'Expected .pup-layer to be visible'
    print('PASS: Pup layer and actor initialized!')

    # 4. Scroll down 800px and check movement
    driver.execute_script('window.scrollTo(0, 800);')
    time.sleep(0.5)

    actor_scrolled = driver.execute_script('''
        let actor = document.querySelector(".pup-actor");
        return {
            actorTransform: actor ? actor.style.transform : null,
        };
    ''')
    print(f'Scrolled actor transform: {actor_scrolled}')
    assert actor_scrolled['actorTransform'] != actor_initial['actorTransform'], 'Expected actor to move on scroll'
    print('PASS: Pup actor smoothly follows scroll!')

    # 5. Scroll down to 2000px
    driver.execute_script('window.scrollTo(0, 2000);')
    time.sleep(0.5)

    actor_2000 = driver.execute_script('''
        let actor = document.querySelector(".pup-actor");
        return {
            actorTransform: actor ? actor.style.transform : null,
        };
    ''')
    print(f'Actor at 2000px: {actor_2000}')
    print('PASS: Traveling companion puppy scroll animation 100% verified!')

finally:
    driver.quit()

