"""這支程式會開啟國泰世華網站"""

import time
import os
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
input_element = driver.find_element(By.XPATH, "//*[text()='產品介紹']")
input_element.click()
input_element = driver.find_element(By.XPATH, "//*[text()='信用卡']")
input_element.click()
input_element = driver.find_element(By.XPATH, "//*[text()='卡片介紹']")
input_element.click()
time.sleep(1)
a_element = driver.find_element(By.XPATH, "//a//p[text()='停發卡']")
# 滾動tab頁籤到元素可見（避免被 swiper 隱藏）
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'})", a_element)
time.sleep(1)
a_element.click()
time.sleep(2)

# 計算停發信用卡數量
bullets = driver.find_elements(By.XPATH,"//h2[text()='停發卡']/following::span[contains(@class, 'swiper-pagination-bullet')]")
print(f"停發信用卡：{len(bullets)}")

# 建立截圖資料夾
output_dir = "停發卡_截圖"
os.makedirs(output_dir, exist_ok=True)

# 遍歷停發信用卡並截圖保存
for i in range(len(bullets)):
    try:
        # 重新抓取停發信用卡
        bullet = driver.find_elements(By.XPATH,"//h2[text()='停發卡']/following::span[contains(@class, 'swiper-pagination-bullet')]")[i]
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(bullet))
        time.sleep(0.3)
        bullet.click()
        time.sleep(1)

        # 截圖並保存，每建一個檔名就加1
        screenshot_path = os.path.join(output_dir, f"停發信用卡_{i+1}.png")
        driver.save_screenshot(screenshot_path)

    except Exception as e:
        print(f"點擊第 {i+1} 個 停發信用卡 失敗：{e}")

# 比對停發信用卡數量與截圖數量相同
screenshot_files = [f for f in os.listdir(output_dir) if f.endswith(".png")]
if len(screenshot_files) == len(bullets):
    print(f"比對數量一致，共有 {len(screenshot_files)} 張")
else:
    print(f"比對數量不一致，停發信用卡{len(bullets)} 個，截圖有：{len(screenshot_files)} 張")

# 等待幾秒看結果
time.sleep(2)

# 關閉瀏覽器
driver.quit()