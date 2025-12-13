from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path = r"F:/Satish/chromedriver-win64/chromedriver.exe"   # UPDATE THIS

def main():
    driver = webdriver.Chrome(service=Service(driver_path))
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")

        # -----------------------
        # 1. Simple Alert
        # -----------------------
        driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
        alert = driver.switch_to.alert
        print("Alert Text:", alert.text)
        alert.accept()

        result = driver.find_element(By.ID, "result").text
        print("Result:", result)

        # -----------------------
        # 2. Confirm Alert
        # -----------------------
        driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        alert = driver.switch_to.alert
        print("Confirm Text:", alert.text)
        alert.dismiss()

        result = driver.find_element(By.ID, "result").text
        print("Result:", result)

        # -----------------------
        # 3. Prompt Alert
        # -----------------------
        driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
        alert = driver.switch_to.alert
        alert.send_keys("Satish")
        alert.accept()

        result = driver.find_element(By.ID, "result").text
        print("Result:", result)

        print("Alert handling test PASSED")

    finally:
        time.sleep(1)
        driver.quit()

if __name__ == "__main__":
    main()
