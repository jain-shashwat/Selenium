from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_drive_path = Service("E:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service= chrome_drive_path)
driver.get("https://www.python.org/")

event_dic = {}

all_time = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
all_event = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li  a")

for n in range(len(all_event)):
    event_dic[n+1] = {
        "time": all_time[n].text,
        "name": all_event[n].text,
    }

print(event_dic)














