"""這支程式會開啟國泰世華網站"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 設定模擬手機裝置
mobile_emulation = { "deviceName": "iPhone X" }
options = Options()
options.add_experimental_option("mobileEmulation", mobile_emulation)

# 啟動 Chrome 模擬手機
driver = webdriver.Chrome(options=options)

# 開啟 國泰世華網站
driver.get("https://www.cathaybk.com.tw/cathaybk/")

time.sleep(3)

# 進入信用卡列表選單
input_element = driver.find_element(By.XPATH, "//*[contains(@class, 'menu-mb-btn flex cursor-pointer tablet:hidden')]")
input_element.click()
time.sleep(2)
input_element = driver.find_element(By.XPATH, "//*[text()='產品介紹']")
input_element.click()
input_element = driver.find_element(By.XPATH, "//*[text()='信用卡']")
input_element.click()

# 計算信用卡子選單有幾個項目
time.sleep(2)
submenu_items = driver.find_elements(By.XPATH, "//div[.='信用卡']/following-sibling::div//a[@target='_self' or @target='_block']")
print(f"信用卡子選單項目數量：{len(submenu_items)}")

# 截圖
driver.save_screenshot("cathay_page2.png")  # 儲存為當前目錄的檔案

# 等待幾秒看結果
time.sleep(3)

# 關閉瀏覽器
driver.quit()