"""這支程式會開啟國泰世華網站"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
mobile_emulation = { "deviceName": "iPhone X" }
options = Options()
options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(options=options)

driver.get("https://www.cathaybk.com.tw/cathaybk/")

time.sleep(5)

driver.save_screenshot("cathay_page1.png")
driver.quit()
