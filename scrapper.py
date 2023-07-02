from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pprint import pprint

timeout = 5
options = Options()
options.add_argument('--headless')

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


def get_grid_reference(postcode):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get(url)
    post_code_input = driver.find_element(By.ID, "txtPostcode")
    post_code_input.clear()
    post_code_input.send_keys(postcode)
    driver.find_element(By.ID, "find1").click()
    # getting the grid reference
    data_table = driver.find_element(By.ID, "tbl")
    try:
        element_present = EC.presence_of_element_located((By.ID, "row1"))
        WebDriverWait(driver, timeout).until(element_present)
        grid_row = data_table.find_element(By.ID, "row1")
        grid_input_value = grid_row.find_element(By.TAG_NAME, "input").get_attribute("value")
    except TimeoutException:
        grid_input_value = "No data found for this postcode"
    pprint(f"Grid reference for {postcode} is {grid_input_value}")
    driver.quit()
    return grid_input_value

# get_grid_reference("NW103JD")