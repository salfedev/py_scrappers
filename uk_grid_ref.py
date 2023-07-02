#!/usr/bin/env python3
# python3 uk_grid_ref.py "postcode"
# run chmod +x uk_grid_ref.py to make the file executable
# then run ./uk_grid_ref.py "postcode", example: ./uk_grid_ref.py NW103JD

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
# options.headless = True is deprecated!
options.add_argument('--headless')
# don't close the browser after the script is done
# options.add_experimental_option("detach", True)

# disable images, css, js, etc.
prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2, 
                            'plugins': 2, 'popups': 2, 'geolocation': 2, 
                            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2, 
                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2, 
                            'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2, 
                            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 
                            'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 
                            'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 
                            'durable_storage': 2}}
options.add_experimental_option('prefs', prefs)
url = "https://gridreferencefinder.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
}

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get(url)


def get_grid_reference(postcode, row_counter, driver):
    # sending keys to the input
    post_code_input = driver.find_element(By.ID, "txtPostcode")
    post_code_input.clear()
    post_code_input.send_keys(postcode)
    driver.find_element(By.ID, "find1").click()
    # getting the grid reference
    data_table = driver.find_element(By.ID, "tbl")
    try:
        element_present = EC.presence_of_element_located((By.ID, f"row{row_counter}"))
        WebDriverWait(driver, timeout).until(element_present)
        grid_row = data_table.find_element(By.ID, f"row{row_counter}")
        grid_input_value = grid_row.find_element(By.TAG_NAME, "input")
    except TimeoutException:
        grid_input_value = "No data found for this postcode"
        # print("Timed out waiting for page to load")
    # except Exception as e:
    #     print(e)    
    # finally
    print('Grid Reference: ' + red.bold(grid_input_value.get_attribute("value")))
    print(yellow.bold('----------------------------------'))
    


# get_grid_reference(postcode)
row_counter = 1
for arg in argv:
    if arg != argv[0]:
        print(yellow.bold(row_counter) + " " + 'Postcode: ' + arg)
        get_grid_reference(arg, row_counter, driver)
        row_counter += 1

print(green.bold("Done!"))
