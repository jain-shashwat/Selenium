from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_drive_path = Service("E:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service= chrome_drive_path)
driver.get("https://www.amazon.in/Noise-Bluetooth-Calling-Tracking-Detection/dp/B0B5LVS732/ref=sr_1_2?pd_rd_r=a4203e62-956d-4fec-a927-27cbec44572c&pd_rd_w=xG7Ps&pd_rd_wg=96Dq2&pf_rd_p=5365dd31-4e3f-46bc-bd43-0dc1868c425c&pf_rd_r=WH2KHYKR9QCNKK61ZJ6K&qid=1675339807&sr=8-2")
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(price.text)

search_bar = driver.find_element(by=By.NAME,value="field-keywords")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

# link_1 = driver.find_element(by=By.CSS_SELECTOR,value= ".a-spacing-mini a")
# print(link_1.text)
# print(link_1.get_attribute("href"))

link_2 = driver.find_element(by=By.XPATH,value= '//*[@id="merchant-info"]/a[2]')
print(link_2.get_attribute("href"))




# # driver = webdriver.ChromeOptions()
# chrome_drive_path = Service(executable_path="E:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service=chrome_drive_path)
# # driver = webdriver.Chrome(service=service, options=driver)
# driver.get("https://www.amazon.in/Noise-Bluetooth-Calling-Tracking-Detection/dp/B0B5LVS732/ref=sr_1_2?pd_rd_r=a4203e62-956d-4fec-a927-27cbec44572c&pd_rd_w=xG7Ps&pd_rd_wg=96Dq2&pf_rd_p=5365dd31-4e3f-46bc-bd43-0dc1868c425c&pf_rd_r=WH2KHYKR9QCNKK61ZJ6K&qid=1675339807&sr=8-2")
# price = driver.find_element(by=By.CLASS_NAME, value="a-price-whole")
# print(price.text)






























# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# options = Options()
# options.add_argument("start-maximized")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://www.amazon.in")




