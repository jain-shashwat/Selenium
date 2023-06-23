from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = Service("E:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service= chrome_driver_path)
driver.get("https://skidrowcodex.co/")
time.sleep(1)

login_icon = driver.find_element(by=By.CLASS_NAME, value="icon-login")
login_icon.click()

login_name = driver.find_element(by=By.NAME, value="login_name")
# login_name.click()  not needed
login_name.send_keys("SHASHWAT JAIN")
# time.sleep(1)

login_pass = driver.find_element(by=By.NAME, value="login_password")
login_pass.send_keys("Shashwat@123")
# time.sleep(1)

submit = driver.find_element(by=By.CSS_SELECTOR, value='#loginpane > div > ul > li:nth-child(3) > button')
submit.click()
time.sleep(5)