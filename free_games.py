#!/usr/bin/env python3
# python3 free_games.py
# run chmod +x free_games.py to make the file executable
# then run ./free_games.py
# import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pprint import pprint
from simple_chalk import chalk, green, red, yellow, blue, bold, underline
from sys import argv

timeout = 5
options = Options()
options.add_argument("--window-size=1920,1080")
# options.add_argument('--headless')
# don't close the browser after the script is done
# options.add_experimental_option("detach", True)
# options.add_argument("--disable-blink-features=AutomationControlled")

# disable images, css, js, etc.
# prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2,
#                             'plugins': 2, 'popups': 2, 'geolocation': 2,
#                             'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
#                             'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
#                             'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,
#                             'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
#                             'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,
#                             'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,
#                             'durable_storage': 2}}
# options.add_experimental_option('prefs', prefs)

url = "https://www.epicgames.com/store/en-US/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
}

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get(url)
driver.implicitly_wait(5)
# driver.execute_script("window.scrollBy(0,1000)")


element_present = EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Free Now')]"))
driver.get_screenshot_as_file("screenshot.png")
WebDriverWait(driver, timeout).until(element_present)

free_games = driver.find_element(By.XPATH, "//span[text()='Free Now']")

pprint("Free Games:")
pprint(free_games.text)

# free_title = driver.find_element(By.XPATH, "//div[@data-testid='offer-title-info-title']")
free_title = driver.find_element(By.XPATH, "//a[contains(@aria-label, 'Free Games, 1 of 2')]")
free_title2 = driver.find_element(By.XPATH, "//a[contains(@aria-label, 'Free Games, 2 of 2')]")
pprint(free_title.get_attribute('aria-label'))
pprint(free_title2.get_attribute('aria-label'))




# for game in free_games:
#     print(game.text)
