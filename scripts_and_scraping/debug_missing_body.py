from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless=new')
options.add_argument('--window-size=1440,900')
driver = webdriver.Chrome(options=options)

try:
    driver.get('http://localhost:5173/')
    import time
    time.sleep(2.0)
    driver.execute_script('window.scrollTo(0, 800);')
    time.sleep(0.5)

    svg_info = driver.execute_script('''
        let actor = document.querySelector(".pup-actor");
        let body = document.querySelector(".pup-actor__body");
        let svg = body ? body.querySelector("svg") : null;
        if (!svg) return { error: "No svg in .pup-actor__body" };

        let parts = {};
        svg.querySelectorAll("[data-p]").forEach(el => {
            parts[el.dataset.p] = {
                tag: el.tagName,
                transform: el.getAttribute("transform"),
                opacity: el.getAttribute("opacity"),
                style: el.getAttribute("style"),
                bbox: el.getBBox ? { x: el.getBBox().x, y: el.getBBox().y, w: el.getBBox().width, h: el.getBBox().height } : null
            };
        });

        return {
            actorTransform: actor ? actor.style.transform : null,
            bodyTransform: body ? body.style.transform : null,
            svgViewBox: svg.getAttribute("viewBox"),
            svgSize: { w: svg.clientWidth, h: svg.clientHeight },
            parts: parts
        };
    ''')

    print('SVG info when scrolled to 800px:')
    import pprint
    pprint.pprint(svg_info)

finally:
    driver.quit()

