import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PAGES = [
    ("home", "https://puppy.instabizweb.com/", "http://localhost:5173/"),
    ("puppies", "https://puppy.instabizweb.com/puppies", "http://localhost:5173/puppies"),
    ("puppy_detail", "https://puppy.instabizweb.com/puppies/maltipoo-max-male", "http://localhost:5173/puppies/maltipoo-max-male"),
    ("how_it_works", "https://puppy.instabizweb.com/how-it-works", "http://localhost:5173/how-it-works"),
    ("happy_families", "https://puppy.instabizweb.com/happy-families", "http://localhost:5173/happy-families"),
    ("gone_home", "https://puppy.instabizweb.com/gone-home", "http://localhost:5173/gone-home"),
    ("faq", "https://puppy.instabizweb.com/faq", "http://localhost:5173/faq"),
    ("contact", "https://puppy.instabizweb.com/contact", "http://localhost:5173/contact"),
]

os.makedirs("comparison/desktop/original", exist_ok=True)
os.makedirs("comparison/desktop/local", exist_ok=True)
os.makedirs("comparison/mobile/original", exist_ok=True)
os.makedirs("comparison/mobile/local", exist_ok=True)

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1440,900")

driver = webdriver.Chrome(options=chrome_options)

try:
    print("=== CAPTURING DESKTOP (1440x900) ===")
    driver.set_window_size(1440, 900)
    for name, orig_url, local_url in PAGES:
        # 1. Original
        try:
            print(f"[Desktop] Original {name}...")
            driver.get(orig_url)
            time.sleep(2)
            out_orig = os.path.abspath(f"comparison/desktop/original/{name}.png")
            driver.save_screenshot(out_orig)
            print(f"  -> Saved {out_orig}")
        except Exception as e:
            print(f"  Error original {name}: {e}")

        # 2. Local
        try:
            print(f"[Desktop] Local {name}...")
            driver.get(local_url)
            time.sleep(1.5)
            out_local = os.path.abspath(f"comparison/desktop/local/{name}.png")
            driver.save_screenshot(out_local)
            print(f"  -> Saved {out_local}")
        except Exception as e:
            print(f"  Error local {name}: {e}")

    print("\n=== CAPTURING MOBILE (390x844) ===")
    driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", {
        "width": 390,
        "height": 844,
        "deviceScaleFactor": 2,
        "mobile": True
    })

    for name, orig_url, local_url in [("home", PAGES[0][1], PAGES[0][2]), ("puppies", PAGES[1][1], PAGES[1][2]), ("puppy_detail", PAGES[2][1], PAGES[2][2]), ("contact", PAGES[7][1], PAGES[7][2])]:
        # 1. Original
        try:
            print(f"[Mobile] Original {name}...")
            driver.get(orig_url)
            time.sleep(2)
            out_orig = os.path.abspath(f"comparison/mobile/original/{name}.png")
            driver.save_screenshot(out_orig)
            print(f"  -> Saved {out_orig}")
        except Exception as e:
            print(f"  Error original {name}: {e}")

        # 2. Local
        try:
            print(f"[Mobile] Local {name}...")
            driver.get(local_url)
            time.sleep(1.5)
            out_local = os.path.abspath(f"comparison/mobile/local/{name}.png")
            driver.save_screenshot(out_local)
            print(f"  -> Saved {out_local}")
        except Exception as e:
            print(f"  Error local {name}: {e}")

    print("\nAll comparison screenshots captured successfully!")
finally:
    driver.quit()

