#!/usr/bin/env python3
# python3 uk_grid_ref.py "postcode"
# run chmod +x uk_grid_ref.py to make the file executable

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pprint import pprint
from simple_chalk import chalk, green, red, yellow, blue, bold, underline
from sys import argv
# for arg in argv:
#     print('arg :' + arg)

postcode = argv[1]

options = Options()
# options.headless = True is deprecated!
options.add_argument('--headless')
options.add_experimental_option("detach", True)
url = "https://gridreferencefinder.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
}

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


def get_grid_reference(postcode, row_counter, driver):
    driver.get(url)
    # print(yellow.bold(f"{row_counter}: row{row_counter}"))
    # sending keys to the input
    post_code_input = driver.find_element(By.ID, "txtPostcode")
    post_code_input.send_keys(postcode)
    driver.find_element(By.ID, "find1").click()
    # waiting for the page to load
    # driver.implicitly_wait(20)
    # driver.navigate().refresh();
    # getting the table
    data_table = driver.find_element(By.ID, "tbl")
    # pprint(data_table.get_attribute("innerHTML"))
    # rows = data_table.find_elements(By.TAG_NAME, "tr")
    # pprint(data_table.get_attribute("innerHTML"))
    # row = rows[row_counter - 1].find_elements(By.TAG_NAME, "td").find_element(By.TAG_NAME, "input")
    grid_row = data_table.find_element(By.ID, f"row{1}")
    # pprint(grid_row.get_attribute("innerHTML"))
    grid_input_value = grid_row.find_element(By.TAG_NAME, "input")
    # grid_input_value = row
    print(By.ID + ": " + grid_input_value.get_attribute("id"))
    print(yellow.bold('----------------------------------'))
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
