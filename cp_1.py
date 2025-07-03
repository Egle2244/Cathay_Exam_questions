"""這支程式會開啟國泰世華網站"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 設定模擬手機裝置
mobile_emulation = { "deviceName": "iPhone X" }

options = Options()
options.add_experimental_option("mobileEmulation", mobile_emulation)

# 啟動 Chrome 模擬手機
driver = webdriver.Chrome(options=options)

# 開啟 國泰世華網站
driver.get("https://www.cathaybk.com.tw/cathaybk/")

# 等待幾秒看結果
time.sleep(5)

# 截圖
driver.save_screenshot("cathay_page1.png")  # 儲存為當前目錄的檔案

# 關閉瀏覽器
driver.quit()
