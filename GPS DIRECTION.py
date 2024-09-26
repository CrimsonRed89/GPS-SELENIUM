from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import sys
import csv

path = "C:\\Coding1\\Coding\\python\\Automation\\chromedriver-win64\\chrome.exe"

url = "https://www.google.com/maps"

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\aayus\\AppData\\Local\\Google\\Chrome for Testing\\User Data\\Default")
options.add_argument("profile-directory=Default") 
options.binary_location = path

driver = webdriver.Chrome(options)
driver.get(url)

location = sys.argv[1]

time.sleep(5)
def mylocation():
    myloc = driver.find_element(By.ID, "sVuEFc")
    myloc.click()
mylocation()

search_input = driver.find_element(By.CSS_SELECTOR, "input[id='searchboxinput']")
search_input.click()
search_input.send_keys(location)
time.sleep(2)

search_input.send_keys(Keys.ARROW_DOWN)
search_input.send_keys(Keys.RETURN)

time.sleep(2)

direction = driver.find_element(By.CSS_SELECTOR, "button.g88MCb.S9kvJb")
direction.click()
time.sleep(3)
input_field = driver.find_element(By.XPATH, "//input[@aria-label='Choose starting point, or click on the map...']")
input_field.click()
time.sleep(3)
input_field.send_keys("Your location")
input_field.send_keys(Keys.RETURN)
time.sleep(20)

driver.quit()