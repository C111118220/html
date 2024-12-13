＃step 1 爬取網頁的主要程式碼
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_data():
    # 初始化 Safari WebDriver
    driver = webdriver.Safari()

    try:
        # 打開目標網址
        url = "https://webap.nkust.edu.tw/nkust/ag_pro/ag202.jsp"
        driver.get(url)

        # 等待頁面加載
        time.sleep(3)

        # 填寫表單中的選項
        user_campus_input = driver.find_element(By.ID, "cmp_area_id")
        user_degree_input = driver.find_element(By.ID, "dgr_id")

        # 模擬輸入資料
        user_campus_input.send_keys("國立高雄科技大學(第一校區)")
        user_degree_input.send_keys("日間部四技")

        # 模擬提交表單
        submit_button = driver.find_element(By.XPATH, "//input[@type='button' and @value='查詢']")  # 替換為查詢按鈕的 XPath
        submit_button.click()

        # 等待結果加載
        time.sleep(5)

        # 抓取結果資料
        results = driver.find_element(By.TAG_NAME, "body").text
        print("結果資料:\n")
        print(results)

    except Exception as e:
        print(f"發生錯誤: {e}")

    finally:
        # 關閉瀏覽器
        driver.quit()

#step 2 在Ｍac上執行與測試程式碼

from web_scraper_safari import scrape_data

if __name__ == "__main__":
    print("開始執行爬蟲程式...")
    scrape_data()
    print("爬蟲程式執行完成。")







