import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless=new')
options.add_argument('--window-size=1440,900')
driver = webdriver.Chrome(options=options)

try:
    print('Loading https://puppy.instabizweb.com/ ...')
    driver.get('https://puppy.instabizweb.com/')
    time.sleep(3.0)
    
    # Check initial state
    html_attrs_0 = driver.execute_script('return Object.assign({}, document.documentElement.dataset);')
    print('Initial html dataset:', html_attrs_0)
    
    pup_layer_0 = driver.execute_script('''
        let el = document.querySelector(".pup-layer, .pup-actor, [data-pup-scene], [data-pup-stop]");
        return el ? { class: el.className, hidden: el.hidden, html: el.outerHTML.slice(0, 300) } : null;
    ''')
    print('Initial pup_layer / actor:', pup_layer_0)
    
    # Scroll down 500px
    print('Scrolling down 500px...')
    driver.execute_script('window.scrollTo({ top: 500, behavior: "smooth" });')
    time.sleep(1.0)
    
    html_attrs_500 = driver.execute_script('return Object.assign({}, document.documentElement.dataset);')
    print('HTML dataset at 500px:', html_attrs_500)
    
    actor_info_500 = driver.execute_script('''
        let actor = document.querySelector(".pup-actor");
        let layer = document.querySelector(".pup-layer");
        return {
            hasActor: !!actor,
            actorStyle: actor ? actor.getAttribute("style") : null,
            actorClass: actor ? actor.className : null,
            layerHidden: layer ? layer.hidden : null,
            layerStyle: layer ? layer.getAttribute("style") : null,
            layerDataset: layer ? Object.assign({}, layer.dataset) : null,
        };
    ''')
    print('Actor info at 500px:', actor_info_500)

    # Scroll down 1500px
    print('Scrolling down 1500px...')
    driver.execute_script('window.scrollTo({ top: 1500, behavior: "smooth" });')
    time.sleep(1.0)
    
    actor_info_1500 = driver.execute_script('''
        let actor = document.querySelector(".pup-actor");
        let layer = document.querySelector(".pup-layer");
        return {
            actorStyle: actor ? actor.getAttribute("style") : null,
            layerHidden: layer ? layer.hidden : null,
            layerDataset: layer ? Object.assign({}, layer.dataset) : null,
        };
    ''')
    print('Actor info at 1500px:', actor_info_1500)

    # Scroll down 3000px
    print('Scrolling down 3000px...')
    driver.execute_script('window.scrollTo({ top: 3000, behavior: "smooth" });')
    time.sleep(1.0)
    
    actor_info_3000 = driver.execute_script('''
        let actor = document.querySelector(".pup-actor");
        let layer = document.querySelector(".pup-layer");
        return {
            actorStyle: actor ? actor.getAttribute("style") : null,
            layerHidden: layer ? layer.hidden : null,
            layerDataset: layer ? Object.assign({}, layer.dataset) : null,
        };
    ''')
    print('Actor info at 3000px:', actor_info_3000)

finally:
    driver.quit()

