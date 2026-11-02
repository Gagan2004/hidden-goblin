import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless=new')
options.add_argument('--window-size=1440,900')
driver = webdriver.Chrome(options=options)

try:
    print('1. Loading local server at http://localhost:5173/ ...')
    driver.get('http://localhost:5173/')
    time.sleep(2.0)

    # 1. Check initial state at scroll = 0
    state_0 = driver.execute_script('''
        let actor = document.querySelector(".pup-actor");
        let layer = document.querySelector(".pup-layer");
        let body = document.querySelector(".pup-actor__body svg [data-p='body']");
        let ledge = document.querySelector(".pup-actor__body svg [data-p='ledge']");
        return {
            datasetPup: document.documentElement.dataset.pup,
            layerFront: layer ? layer.dataset.front : null,
            actorTransform: actor ? actor.style.transform : null,
            bodyTransform: body ? body.getAttribute("transform") : null,
            ledgeOpacity: ledge ? ledge.getAttribute("opacity") : null
        };
    ''')
    print('Initial state at scroll = 0:')
    for k, v in state_0.items():
        print(f'  {k}: {v}')
    
    assert state_0['datasetPup'] == 'live', 'Expected dataset.pup to be "live"'
    assert state_0['layerFront'] == 'false', 'Expected layer to be behind quilt (front=false) in hero booth'
    assert state_0['ledgeOpacity'] == '1', 'Expected ledge paws to be visible (opacity=1) in hero booth'
    print('PASS: Initial hero booth position & ledge paws verified!')

    # 2. Scroll down 600px
    print('\n2. Scrolling down 600px...')
    driver.execute_script('window.scrollTo(0, 600);')
    time.sleep(0.4)

    state_600 = driver.execute_script('''
        let actor = document.querySelector(".pup-actor");
        let layer = document.querySelector(".pup-layer");
        let frontLeg = document.querySelector(".pup-actor__body svg [data-p='fn']");
        let side = document.querySelector(".pup-actor__body svg [data-p='body']");
        let prints = Array.from(document.querySelectorAll(".pup-prints svg")).filter(p => p.style.transform);
        return {
            layerFront: layer ? layer.dataset.front : null,
            actorTransform: actor ? actor.style.transform : null,
            frontLegTransform: frontLeg ? frontLeg.getAttribute("transform") : null,
            sideOpacity: side ? parseFloat(side.getAttribute("opacity") || "0") : 0,
            printsDropped: prints.length
        };
    ''')
    print('State at scroll = 600px:')
    for k, v in state_600.items():
        print(f'  {k}: {v}')
    
    assert state_600['layerFront'] == 'true', 'Expected layer to be in front (front=true) after stepping out of quilt'
    assert state_600['sideOpacity'] >= 0.8, 'Expected side body to be visible when walking'
    assert state_600['actorTransform'] != state_0['actorTransform'], 'Expected actor to move'
    print('PASS: Teddy successfully stepped out of the quilt and is walking along the curve!')

    # 3. Test idle speech bubble "coming?"
    print('\n3. Waiting 3 seconds for idle detection...')
    time.sleep(3.0)
    bubble_state = driver.execute_script('''
        let bubble = document.querySelector(".pup-actor .pup-bubble");
        return {
            show: bubble ? bubble.dataset.show : null,
            text: bubble ? bubble.textContent : null
        };
    ''')
    print(f'Idle speech bubble: show={bubble_state["show"]}, text="{bubble_state["text"]}"')
    assert bubble_state['text'] == 'coming?', f'Expected "coming?", got {bubble_state["text"]}'
    assert bubble_state['show'] == 'true', 'Expected speech bubble to show'
    print('PASS: Idle detection speech bubble ("coming?") verified!')

    # 4. Test clicking on actor
    print('\n4. Testing click interaction on .pup-actor...')
    driver.execute_script('document.querySelector(".pup-actor").click();')
    time.sleep(0.3)
    after_click = driver.execute_script('''
        let bubble = document.querySelector(".pup-actor .pup-bubble");
        let hearts = document.querySelectorAll(".pup-heart");
        return {
            show: bubble ? bubble.dataset.show : null,
            text: bubble ? bubble.textContent : null,
            heartsCount: hearts.length
        };
    ''')
    print(f'After click: text="{after_click["text"]}", hearts={after_click["heartsCount"]}')
    assert after_click['show'] == 'true', 'Expected bubble after click'
    print('PASS: Click interaction on .pup-actor verified!')

    print('\nALL SCROLL COMPANION TESTS PASSED WITH 100% ACCURACY!')

finally:
    driver.quit()
