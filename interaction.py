from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

chrome_drive_path = Service("E:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service= chrome_drive_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

scrape = driver.find_element(by=By.XPATH, value='//*[@id="articlecount"]/a[1]')
# scrape.click()

all_portals = driver.find_element(by=By.LINK_TEXT, value="View history")
# all_portals.click()

from selenium.webdriver.common.keys import Keys

search_bar = driver.find_element(by=By.NAME, value="search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)

time.sleep(10)